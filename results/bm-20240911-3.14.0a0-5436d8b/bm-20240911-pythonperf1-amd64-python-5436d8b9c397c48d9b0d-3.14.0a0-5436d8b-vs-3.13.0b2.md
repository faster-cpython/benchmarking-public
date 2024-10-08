# Results vs. 3.13.0b2

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: windows-amd64
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 221 ms: 1.07x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 39.4 ms: 1.12x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 83.3 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg | 605 ms                                                          | 553 ms: 1.09x faster                                                       |
| async_tree_none  | 218 ms                                                          | 207 ms: 1.05x faster                                                       |
| async_tree_io    | 588 ms                                                          | 564 ms: 1.04x faster                                                       |
| Geometric mean   | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 54.4 ms: 1.09x slower                                                      |
| nbody          | 67.6 ms                                                         | 79.8 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                      |
| regex_dna      | 119 ms                                                          | 114 ms: 1.04x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 89.6 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.28 us: 1.02x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.5 us: 1.03x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.6 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.8 ms: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.77 us: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.2 ms: 1.08x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 19.7 us: 1.09x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.18 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 40.4 ms: 1.11x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.43 us: 1.12x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.56 sec: 1.15x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 145 us: 1.19x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 209 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.3 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.3 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.83 ms: 1.07x slower                                                      |
| django_template | 21.7 ms                                                         | 24.5 ms: 1.13x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 35.9 ms: 1.14x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.9 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 507 us: 15.98x faster                                                      |
| deepcopy                 | 220 us                                                          | 188 us: 1.17x faster                                                       |
| deepcopy_memo            | 22.1 us                                                         | 20.0 us: 1.11x faster                                                      |
| async_tree_io_tg         | 605 ms                                                          | 553 ms: 1.09x faster                                                       |
| regex_v8                 | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                      |
| async_tree_none          | 218 ms                                                          | 207 ms: 1.05x faster                                                       |
| regex_dna                | 119 ms                                                          | 114 ms: 1.04x faster                                                       |
| async_tree_io            | 588 ms                                                          | 564 ms: 1.04x faster                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 1.92 us: 1.04x faster                                                      |
| pathlib                  | 75.9 ms                                                         | 73.9 ms: 1.03x faster                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| gc_traversal             | 1.55 ms                                                         | 1.52 ms: 1.02x faster                                                      |
| pidigits                 | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| sqlite_synth             | 1.60 us                                                         | 1.62 us: 1.01x slower                                                      |
| spectral_norm            | 63.7 ms                                                         | 64.7 ms: 1.01x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 65.8 ms: 1.02x slower                                                      |
| tornado_http             | 81.8 ms                                                         | 83.3 ms: 1.02x slower                                                      |
| pickle                   | 7.11 us                                                         | 7.28 us: 1.02x slower                                                      |
| json_loads               | 14.2 us                                                         | 14.5 us: 1.03x slower                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 93.6 ms: 1.03x slower                                                      |
| go                       | 82.1 ms                                                         | 84.6 ms: 1.03x slower                                                      |
| crypto_pyaes             | 45.5 ms                                                         | 46.9 ms: 1.03x slower                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 64.8 ms: 1.04x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| python_startup           | 20.3 ms                                                         | 21.3 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.64 ms: 1.05x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 810 us: 1.06x slower                                                       |
| unpickle_list            | 2.62 us                                                         | 2.77 us: 1.06x slower                                                      |
| sympy_sum                | 84.4 ms                                                         | 89.2 ms: 1.06x slower                                                      |
| sympy_integrate          | 12.2 ms                                                         | 13.0 ms: 1.06x slower                                                      |
| async_generators         | 223 ms                                                          | 238 ms: 1.06x slower                                                       |
| 2to3                     | 207 ms                                                          | 221 ms: 1.07x slower                                                       |
| python_startup_no_site   | 16.2 ms                                                         | 17.3 ms: 1.07x slower                                                      |
| logging_format           | 6.22 us                                                         | 6.66 us: 1.07x slower                                                      |
| generators               | 19.6 ms                                                         | 20.9 ms: 1.07x slower                                                      |
| mako                     | 6.36 ms                                                         | 6.83 ms: 1.07x slower                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 57.2 ms: 1.08x slower                                                      |
| logging_simple           | 5.78 us                                                         | 6.25 us: 1.08x slower                                                      |
| pylint                   | 205 ms                                                          | 222 ms: 1.08x slower                                                       |
| telco                    | 4.67 ms                                                         | 5.06 ms: 1.08x slower                                                      |
| pickle_dict              | 18.1 us                                                         | 19.7 us: 1.09x slower                                                      |
| scimark_lu               | 56.6 ms                                                         | 61.8 ms: 1.09x slower                                                      |
| float                    | 49.7 ms                                                         | 54.4 ms: 1.09x slower                                                      |
| typing_runtime_protocols | 101 us                                                          | 111 us: 1.10x slower                                                       |
| coroutines               | 12.8 ms                                                         | 14.0 ms: 1.10x slower                                                      |
| sqlglot_optimize         | 32.7 ms                                                         | 36.0 ms: 1.10x slower                                                      |
| comprehensions           | 10.4 us                                                         | 11.4 us: 1.10x slower                                                      |
| json_dumps               | 5.61 ms                                                         | 6.18 ms: 1.10x slower                                                      |
| chaos                    | 38.4 ms                                                         | 42.3 ms: 1.10x slower                                                      |
| dulwich_log              | 38.0 ms                                                         | 41.9 ms: 1.10x slower                                                      |
| sqlglot_normalize        | 173 ms                                                          | 191 ms: 1.10x slower                                                       |
| xml_etree_process        | 36.4 ms                                                         | 40.4 ms: 1.11x slower                                                      |
| sympy_str                | 159 ms                                                          | 176 ms: 1.11x slower                                                       |
| nqueens                  | 56.7 ms                                                         | 62.9 ms: 1.11x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 77.6 ms: 1.11x slower                                                      |
| unpickle                 | 8.40 us                                                         | 9.43 us: 1.12x slower                                                      |
| html5lib                 | 35.0 ms                                                         | 39.4 ms: 1.12x slower                                                      |
| pyflate                  | 279 ms                                                          | 315 ms: 1.13x slower                                                       |
| sympy_expand             | 271 ms                                                          | 306 ms: 1.13x slower                                                       |
| django_template          | 21.7 ms                                                         | 24.5 ms: 1.13x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 35.9 ms: 1.14x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 1.09 ms: 1.14x slower                                                      |
| pprint_safe_repr         | 474 ms                                                          | 541 ms: 1.14x slower                                                       |
| mdp                      | 1.31 sec                                                        | 1.50 sec: 1.14x slower                                                     |
| coverage                 | 42.1 ms                                                         | 48.1 ms: 1.14x slower                                                      |
| pprint_pformat           | 966 ms                                                          | 1.11 sec: 1.15x slower                                                     |
| regex_compile            | 78.0 ms                                                         | 89.6 ms: 1.15x slower                                                      |
| fannkuch                 | 243 ms                                                          | 280 ms: 1.15x slower                                                       |
| raytrace                 | 162 ms                                                          | 187 ms: 1.15x slower                                                       |
| tomli_loads              | 1.35 sec                                                        | 1.56 sec: 1.15x slower                                                     |
| hexiom                   | 3.72 ms                                                         | 4.30 ms: 1.15x slower                                                      |
| scimark_sor              | 75.3 ms                                                         | 87.5 ms: 1.16x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 875 us: 1.17x slower                                                       |
| logging_silent           | 52.9 ns                                                         | 61.9 ns: 1.17x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 16.9 ms: 1.17x slower                                                      |
| nbody                    | 67.6 ms                                                         | 79.8 ms: 1.18x slower                                                      |
| unpickle_pure_python     | 122 us                                                          | 145 us: 1.19x slower                                                       |
| richards                 | 26.7 ms                                                         | 31.7 ms: 1.19x slower                                                      |
| deltablue                | 1.88 ms                                                         | 2.24 ms: 1.19x slower                                                      |
| richards_super           | 30.2 ms                                                         | 35.8 ms: 1.19x slower                                                      |
| scimark_fft              | 171 ms                                                          | 204 ms: 1.19x slower                                                       |
| pickle_pure_python       | 175 us                                                          | 209 us: 1.19x slower                                                       |
| scimark_monte_carlo      | 39.1 ms                                                         | 48.5 ms: 1.24x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (11): async_tree_memoization_tg, json, async_tree_none_tg, async_tree_memoization, asyncio_tcp, pycparser, async_tree_cpu_io_mixed, create_gc_cycles, asyncio_tcp_ssl, pickle_list, async_tree_cpu_io_mixed_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown