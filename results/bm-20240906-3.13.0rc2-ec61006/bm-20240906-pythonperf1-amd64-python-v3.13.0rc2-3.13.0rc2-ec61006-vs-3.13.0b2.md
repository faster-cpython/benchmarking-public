# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc2
- machine: windows-amd64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 216 ms: 1.05x slower                                              |
| chameleon      | 4.80 ms                                                         | 4.89 ms: 1.02x slower                                             |
| docutils       | 1.63 sec                                                        | 1.67 sec: 1.03x slower                                            |
| html5lib       | 35.0 ms                                                         | 39.8 ms: 1.14x slower                                             |
| tornado_http   | 81.8 ms                                                         | 92.6 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                           | 1.07x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none        | 218 ms                                                          | 222 ms: 1.02x slower                                              |
| async_tree_memoization | 264 ms                                                          | 273 ms: 1.03x slower                                              |
| async_tree_none_tg     | 202 ms                                                          | 209 ms: 1.04x slower                                              |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                      |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 68.0 ms: 1.01x slower                                             |
| float          | 49.7 ms                                                         | 50.1 ms: 1.01x slower                                             |
| pidigits       | 150 ms                                                          | 152 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                           | 1.01x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                             |
| regex_compile  | 78.0 ms                                                         | 82.0 ms: 1.05x slower                                             |
| regex_dna      | 119 ms                                                          | 126 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                           | 1.03x slower                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 6.91 us: 1.03x faster                                             |
| unpickle_list        | 2.62 us                                                         | 2.60 us: 1.01x faster                                             |
| json_loads           | 14.2 us                                                         | 14.1 us: 1.01x faster                                             |
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.02x slower                                             |
| xml_etree_parse      | 90.9 ms                                                         | 92.9 ms: 1.02x slower                                             |
| xml_etree_generate   | 53.2 ms                                                         | 54.4 ms: 1.02x slower                                             |
| tomli_loads          | 1.35 sec                                                        | 1.38 sec: 1.03x slower                                            |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.2 ms: 1.03x slower                                             |
| json_dumps           | 5.61 ms                                                         | 5.80 ms: 1.03x slower                                             |
| unpickle_pure_python | 122 us                                                          | 126 us: 1.03x slower                                              |
| xml_etree_process    | 36.4 ms                                                         | 37.8 ms: 1.04x slower                                             |
| unpickle             | 8.40 us                                                         | 8.78 us: 1.04x slower                                             |
| pickle_pure_python   | 175 us                                                          | 185 us: 1.06x slower                                              |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                      |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                             |
| python_startup_no_site | 16.2 ms                                                         | 17.9 ms: 1.11x slower                                             |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 31.6 ms                                                         | 32.0 ms: 1.01x slower                                             |
| django_template | 21.7 ms                                                         | 22.1 ms: 1.02x slower                                             |
| mako            | 6.36 ms                                                         | 6.50 ms: 1.02x slower                                             |
| genshi_text     | 14.4 ms                                                         | 15.2 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                      |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pylint                   | 205 ms                                                          | 186 ms: 1.10x faster                                              |
| json                     | 3.19 ms                                                         | 2.98 ms: 1.07x faster                                             |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.35 ms: 1.06x faster                                             |
| spectral_norm            | 63.7 ms                                                         | 61.2 ms: 1.04x faster                                             |
| pickle                   | 7.11 us                                                         | 6.91 us: 1.03x faster                                             |
| logging_format           | 6.22 us                                                         | 6.09 us: 1.02x faster                                             |
| richards_super           | 30.2 ms                                                         | 29.5 ms: 1.02x faster                                             |
| logging_simple           | 5.78 us                                                         | 5.67 us: 1.02x faster                                             |
| crypto_pyaes             | 45.5 ms                                                         | 44.6 ms: 1.02x faster                                             |
| richards                 | 26.7 ms                                                         | 26.2 ms: 1.02x faster                                             |
| unpickle_list            | 2.62 us                                                         | 2.60 us: 1.01x faster                                             |
| json_loads               | 14.2 us                                                         | 14.1 us: 1.01x faster                                             |
| flaskblogging            | 2.03 sec                                                        | 2.04 sec: 1.00x slower                                            |
| scimark_fft              | 171 ms                                                          | 172 ms: 1.01x slower                                              |
| nbody                    | 67.6 ms                                                         | 68.0 ms: 1.01x slower                                             |
| hexiom                   | 3.72 ms                                                         | 3.75 ms: 1.01x slower                                             |
| logging_silent           | 52.9 ns                                                         | 53.3 ns: 1.01x slower                                             |
| sqlglot_normalize        | 173 ms                                                          | 174 ms: 1.01x slower                                              |
| float                    | 49.7 ms                                                         | 50.1 ms: 1.01x slower                                             |
| deltablue                | 1.88 ms                                                         | 1.90 ms: 1.01x slower                                             |
| sqlite_synth             | 1.60 us                                                         | 1.61 us: 1.01x slower                                             |
| coroutines               | 12.8 ms                                                         | 12.9 ms: 1.01x slower                                             |
| deepcopy_reduce          | 1.99 us                                                         | 2.02 us: 1.01x slower                                             |
| nqueens                  | 56.7 ms                                                         | 57.3 ms: 1.01x slower                                             |
| pyflate                  | 279 ms                                                          | 282 ms: 1.01x slower                                              |
| genshi_xml               | 31.6 ms                                                         | 32.0 ms: 1.01x slower                                             |
| pidigits                 | 150 ms                                                          | 152 ms: 1.01x slower                                              |
| create_gc_cycles         | 888 us                                                          | 901 us: 1.01x slower                                              |
| sqlglot_optimize         | 32.7 ms                                                         | 33.2 ms: 1.02x slower                                             |
| telco                    | 4.67 ms                                                         | 4.74 ms: 1.02x slower                                             |
| pickle_dict              | 18.1 us                                                         | 18.4 us: 1.02x slower                                             |
| chameleon                | 4.80 ms                                                         | 4.89 ms: 1.02x slower                                             |
| deepcopy                 | 220 us                                                          | 223 us: 1.02x slower                                              |
| fannkuch                 | 243 ms                                                          | 248 ms: 1.02x slower                                              |
| django_template          | 21.7 ms                                                         | 22.1 ms: 1.02x slower                                             |
| async_tree_none          | 218 ms                                                          | 222 ms: 1.02x slower                                              |
| xml_etree_parse          | 90.9 ms                                                         | 92.9 ms: 1.02x slower                                             |
| mako                     | 6.36 ms                                                         | 6.50 ms: 1.02x slower                                             |
| xml_etree_generate       | 53.2 ms                                                         | 54.4 ms: 1.02x slower                                             |
| sympy_integrate          | 12.2 ms                                                         | 12.5 ms: 1.02x slower                                             |
| regex_effbot             | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                             |
| tomli_loads              | 1.35 sec                                                        | 1.38 sec: 1.03x slower                                            |
| deepcopy_memo            | 22.1 us                                                         | 22.7 us: 1.03x slower                                             |
| docutils                 | 1.63 sec                                                        | 1.67 sec: 1.03x slower                                            |
| xml_etree_iterparse      | 62.3 ms                                                         | 64.2 ms: 1.03x slower                                             |
| typing_runtime_protocols | 101 us                                                          | 104 us: 1.03x slower                                              |
| sqlglot_transpile        | 955 us                                                          | 985 us: 1.03x slower                                              |
| generators               | 19.6 ms                                                         | 20.2 ms: 1.03x slower                                             |
| json_dumps               | 5.61 ms                                                         | 5.80 ms: 1.03x slower                                             |
| unpickle_pure_python     | 122 us                                                          | 126 us: 1.03x slower                                              |
| meteor_contest           | 69.9 ms                                                         | 72.2 ms: 1.03x slower                                             |
| async_tree_memoization   | 264 ms                                                          | 273 ms: 1.03x slower                                              |
| sympy_sum                | 84.4 ms                                                         | 87.3 ms: 1.04x slower                                             |
| mypy2                    | 418 ms                                                          | 433 ms: 1.04x slower                                              |
| async_tree_none_tg       | 202 ms                                                          | 209 ms: 1.04x slower                                              |
| xml_etree_process        | 36.4 ms                                                         | 37.8 ms: 1.04x slower                                             |
| async_generators         | 223 ms                                                          | 232 ms: 1.04x slower                                              |
| pprint_pformat           | 966 ms                                                          | 1.01 sec: 1.04x slower                                            |
| pprint_safe_repr         | 474 ms                                                          | 494 ms: 1.04x slower                                              |
| go                       | 82.1 ms                                                         | 85.7 ms: 1.04x slower                                             |
| unpickle                 | 8.40 us                                                         | 8.78 us: 1.04x slower                                             |
| 2to3                     | 207 ms                                                          | 216 ms: 1.05x slower                                              |
| pathlib                  | 75.9 ms                                                         | 79.6 ms: 1.05x slower                                             |
| bench_mp_pool            | 64.8 ms                                                         | 68.0 ms: 1.05x slower                                             |
| regex_compile            | 78.0 ms                                                         | 82.0 ms: 1.05x slower                                             |
| genshi_text              | 14.4 ms                                                         | 15.2 ms: 1.05x slower                                             |
| pickle_pure_python       | 175 us                                                          | 185 us: 1.06x slower                                              |
| regex_dna                | 119 ms                                                          | 126 ms: 1.06x slower                                              |
| sqlglot_parse            | 748 us                                                          | 793 us: 1.06x slower                                              |
| sympy_str                | 159 ms                                                          | 169 ms: 1.06x slower                                              |
| aiohttp                  | 889 us                                                          | 946 us: 1.06x slower                                              |
| thrift                   | 8.11 ms                                                         | 8.64 ms: 1.07x slower                                             |
| scimark_monte_carlo      | 39.1 ms                                                         | 41.8 ms: 1.07x slower                                             |
| sympy_expand             | 271 ms                                                          | 291 ms: 1.07x slower                                              |
| bench_thread_pool        | 768 us                                                          | 832 us: 1.08x slower                                              |
| coverage                 | 42.1 ms                                                         | 46.0 ms: 1.09x slower                                             |
| python_startup           | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                             |
| asyncio_tcp_ssl          | 1.48 sec                                                        | 1.63 sec: 1.10x slower                                            |
| dulwich_log              | 38.0 ms                                                         | 42.0 ms: 1.10x slower                                             |
| python_startup_no_site   | 16.2 ms                                                         | 17.9 ms: 1.11x slower                                             |
| asyncio_tcp              | 471 ms                                                          | 530 ms: 1.12x slower                                              |
| tornado_http             | 81.8 ms                                                         | 92.6 ms: 1.13x slower                                             |
| mdp                      | 1.31 sec                                                        | 1.49 sec: 1.13x slower                                            |
| html5lib                 | 35.0 ms                                                         | 39.8 ms: 1.14x slower                                             |
| Geometric mean           | (ref)                                                           | 1.03x slower                                                      |

Benchmark hidden because not significant (14): regex_v8, pycparser, gc_traversal, raytrace, async_tree_cpu_io_mixed_tg, scimark_lu, scimark_sor, chaos, async_tree_cpu_io_mixed, comprehensions, async_tree_io, async_tree_io_tg, pickle_list, async_tree_memoization_tg
Ignored benchmarks (1) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown