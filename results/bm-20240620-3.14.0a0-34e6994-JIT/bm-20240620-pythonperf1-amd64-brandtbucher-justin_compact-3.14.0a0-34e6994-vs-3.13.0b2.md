# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: windows-amd64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.03x faster
- HPT reliability: 98.55%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.73 sec: 1.06x slower                                                     |
| html5lib       | 35.0 ms                                                         | 36.3 ms: 1.04x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 83.3 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg       | 605 ms                                                          | 597 ms: 1.01x faster                                                       |
| async_tree_memoization | 264 ms                                                          | 272 ms: 1.03x slower                                                       |
| async_tree_none        | 218 ms                                                          | 227 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 50.6 ms: 1.34x faster                                                      |
| float          | 49.7 ms                                                         | 44.5 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                           | 1.14x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 116 ms: 1.02x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 82.2 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.18 sec: 1.14x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 50.4 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 59.7 ms: 1.04x faster                                                      |
| pickle_pure_python   | 175 us                                                          | 168 us: 1.04x faster                                                       |
| pickle_list          | 2.90 us                                                         | 2.80 us: 1.04x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.6 us: 1.03x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 35.6 ms: 1.02x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.1 us: 1.01x faster                                                      |
| unpickle_pure_python | 122 us                                                          | 123 us: 1.01x slower                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 92.2 ms: 1.01x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.70 ms: 1.02x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.70 us: 1.04x slower                                                      |
| pickle               | 7.11 us                                                         | 7.49 us: 1.05x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.86 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.24 ms: 1.21x faster                                                      |
| django_template | 21.7 ms                                                         | 24.0 ms: 1.11x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.4 ms: 1.14x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 37.9 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 505 us: 16.06x faster                                                      |
| deepcopy_memo            | 22.1 us                                                         | 15.6 us: 1.42x faster                                                      |
| spectral_norm            | 63.7 ms                                                         | 45.1 ms: 1.41x faster                                                      |
| nbody                    | 67.6 ms                                                         | 50.6 ms: 1.34x faster                                                      |
| deepcopy                 | 220 us                                                          | 168 us: 1.31x faster                                                       |
| mako                     | 6.36 ms                                                         | 5.24 ms: 1.21x faster                                                      |
| deepcopy_reduce          | 1.99 us                                                         | 1.72 us: 1.16x faster                                                      |
| tomli_loads              | 1.35 sec                                                        | 1.18 sec: 1.14x faster                                                     |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.21 ms: 1.13x faster                                                      |
| float                    | 49.7 ms                                                         | 44.5 ms: 1.12x faster                                                      |
| scimark_fft              | 171 ms                                                          | 154 ms: 1.11x faster                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 41.1 ms: 1.11x faster                                                      |
| fannkuch                 | 243 ms                                                          | 220 ms: 1.11x faster                                                       |
| pyflate                  | 279 ms                                                          | 253 ms: 1.10x faster                                                       |
| json                     | 3.19 ms                                                         | 2.94 ms: 1.08x faster                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 50.4 ms: 1.05x faster                                                      |
| logging_format           | 6.22 us                                                         | 5.94 us: 1.05x faster                                                      |
| scimark_monte_carlo      | 39.1 ms                                                         | 37.4 ms: 1.05x faster                                                      |
| logging_simple           | 5.78 us                                                         | 5.53 us: 1.05x faster                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 59.7 ms: 1.04x faster                                                      |
| pickle_pure_python       | 175 us                                                          | 168 us: 1.04x faster                                                       |
| telco                    | 4.67 ms                                                         | 4.49 ms: 1.04x faster                                                      |
| pprint_pformat           | 966 ms                                                          | 932 ms: 1.04x faster                                                       |
| pickle_list              | 2.90 us                                                         | 2.80 us: 1.04x faster                                                      |
| pickle_dict              | 18.1 us                                                         | 17.6 us: 1.03x faster                                                      |
| comprehensions           | 10.4 us                                                         | 10.1 us: 1.03x faster                                                      |
| pprint_safe_repr         | 474 ms                                                          | 460 ms: 1.03x faster                                                       |
| xml_etree_process        | 36.4 ms                                                         | 35.6 ms: 1.02x faster                                                      |
| regex_dna                | 119 ms                                                          | 116 ms: 1.02x faster                                                       |
| regex_effbot             | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| async_tree_io_tg         | 605 ms                                                          | 597 ms: 1.01x faster                                                       |
| sqlite_synth             | 1.60 us                                                         | 1.58 us: 1.01x faster                                                      |
| json_loads               | 14.2 us                                                         | 14.1 us: 1.01x faster                                                      |
| pathlib                  | 75.9 ms                                                         | 75.3 ms: 1.01x faster                                                      |
| generators               | 19.6 ms                                                         | 19.7 ms: 1.01x slower                                                      |
| gc_traversal             | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| unpickle_pure_python     | 122 us                                                          | 123 us: 1.01x slower                                                       |
| nqueens                  | 56.7 ms                                                         | 57.2 ms: 1.01x slower                                                      |
| coroutines               | 12.8 ms                                                         | 12.9 ms: 1.01x slower                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 92.2 ms: 1.01x slower                                                      |
| json_dumps               | 5.61 ms                                                         | 5.70 ms: 1.02x slower                                                      |
| create_gc_cycles         | 888 us                                                          | 903 us: 1.02x slower                                                       |
| tornado_http             | 81.8 ms                                                         | 83.3 ms: 1.02x slower                                                      |
| async_tree_memoization   | 264 ms                                                          | 272 ms: 1.03x slower                                                       |
| logging_silent           | 52.9 ns                                                         | 54.7 ns: 1.03x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 72.3 ms: 1.03x slower                                                      |
| html5lib                 | 35.0 ms                                                         | 36.3 ms: 1.04x slower                                                      |
| unpickle                 | 8.40 us                                                         | 8.70 us: 1.04x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 991 us: 1.04x slower                                                       |
| async_tree_none          | 218 ms                                                          | 227 ms: 1.04x slower                                                       |
| raytrace                 | 162 ms                                                          | 169 ms: 1.04x slower                                                       |
| sqlglot_parse            | 748 us                                                          | 781 us: 1.04x slower                                                       |
| pickle                   | 7.11 us                                                         | 7.49 us: 1.05x slower                                                      |
| regex_compile            | 78.0 ms                                                         | 82.2 ms: 1.05x slower                                                      |
| coverage                 | 42.1 ms                                                         | 44.4 ms: 1.06x slower                                                      |
| go                       | 82.1 ms                                                         | 86.7 ms: 1.06x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.73 sec: 1.06x slower                                                     |
| sympy_sum                | 84.4 ms                                                         | 90.1 ms: 1.07x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.40 sec: 1.07x slower                                                     |
| sqlglot_optimize         | 32.7 ms                                                         | 35.0 ms: 1.07x slower                                                      |
| sympy_str                | 159 ms                                                          | 173 ms: 1.09x slower                                                       |
| bench_mp_pool            | 64.8 ms                                                         | 70.6 ms: 1.09x slower                                                      |
| unpickle_list            | 2.62 us                                                         | 2.86 us: 1.09x slower                                                      |
| typing_runtime_protocols | 101 us                                                          | 111 us: 1.10x slower                                                       |
| 2to3                     | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| python_startup           | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| deltablue                | 1.88 ms                                                         | 2.07 ms: 1.10x slower                                                      |
| scimark_sor              | 75.3 ms                                                         | 83.0 ms: 1.10x slower                                                      |
| hexiom                   | 3.72 ms                                                         | 4.12 ms: 1.11x slower                                                      |
| django_template          | 21.7 ms                                                         | 24.0 ms: 1.11x slower                                                      |
| sympy_expand             | 271 ms                                                          | 301 ms: 1.11x slower                                                       |
| sympy_integrate          | 12.2 ms                                                         | 13.7 ms: 1.12x slower                                                      |
| pylint                   | 205 ms                                                          | 229 ms: 1.12x slower                                                       |
| async_generators         | 223 ms                                                          | 250 ms: 1.12x slower                                                       |
| richards_super           | 30.2 ms                                                         | 33.9 ms: 1.12x slower                                                      |
| richards                 | 26.7 ms                                                         | 30.0 ms: 1.12x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 16.4 ms: 1.14x slower                                                      |
| scimark_lu               | 56.6 ms                                                         | 67.7 ms: 1.20x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 37.9 ms: 1.20x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (12): async_tree_memoization_tg, pycparser, asyncio_tcp_ssl, bench_thread_pool, async_tree_cpu_io_mixed_tg, chaos, pidigits, async_tree_none_tg, asyncio_tcp, async_tree_cpu_io_mixed, async_tree_io, regex_v8
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 98.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown