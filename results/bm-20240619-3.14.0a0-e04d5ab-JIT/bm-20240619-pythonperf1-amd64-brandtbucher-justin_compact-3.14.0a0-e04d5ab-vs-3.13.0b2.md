# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: windows-amd64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.02x faster
- HPT reliability: 98.23%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 230 ms: 1.11x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                                     |
| html5lib       | 35.0 ms                                                         | 35.7 ms: 1.02x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 82.9 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none        | 218 ms                                                          | 225 ms: 1.03x slower                                                       |
| async_tree_memoization | 264 ms                                                          | 272 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 52.0 ms: 1.30x faster                                                      |
| float          | 49.7 ms                                                         | 44.2 ms: 1.13x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                      |
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 82.4 ms: 1.06x slower                                                      |
| regex_v8       | 15.8 ms                                                         | 18.5 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.19 sec: 1.14x faster                                                     |
| pickle_pure_python   | 175 us                                                          | 167 us: 1.05x faster                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 51.4 ms: 1.03x faster                                                      |
| pickle_list          | 2.90 us                                                         | 2.83 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.0 ms: 1.02x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.8 us: 1.02x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 35.9 ms: 1.02x faster                                                      |
| json_dumps           | 5.61 ms                                                         | 5.68 ms: 1.01x slower                                                      |
| pickle               | 7.11 us                                                         | 7.27 us: 1.02x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 125 us: 1.03x slower                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 94.1 ms: 1.04x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.86 us: 1.05x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.78 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.19 ms: 1.22x faster                                                      |
| django_template | 21.7 ms                                                         | 24.3 ms: 1.12x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.2 ms: 1.12x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 39.4 ms: 1.25x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 495 us: 16.36x faster                                                      |
| deepcopy_memo            | 22.1 us                                                         | 15.5 us: 1.42x faster                                                      |
| spectral_norm            | 63.7 ms                                                         | 46.7 ms: 1.37x faster                                                      |
| deepcopy                 | 220 us                                                          | 166 us: 1.32x faster                                                       |
| nbody                    | 67.6 ms                                                         | 52.0 ms: 1.30x faster                                                      |
| mako                     | 6.36 ms                                                         | 5.19 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 1.99 us                                                         | 1.70 us: 1.17x faster                                                      |
| tomli_loads              | 1.35 sec                                                        | 1.19 sec: 1.14x faster                                                     |
| scimark_fft              | 171 ms                                                          | 151 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.21 ms: 1.13x faster                                                      |
| crypto_pyaes             | 45.5 ms                                                         | 40.4 ms: 1.13x faster                                                      |
| float                    | 49.7 ms                                                         | 44.2 ms: 1.13x faster                                                      |
| fannkuch                 | 243 ms                                                          | 219 ms: 1.11x faster                                                       |
| pyflate                  | 279 ms                                                          | 254 ms: 1.10x faster                                                       |
| logging_simple           | 5.78 us                                                         | 5.48 us: 1.06x faster                                                      |
| logging_format           | 6.22 us                                                         | 5.91 us: 1.05x faster                                                      |
| pickle_pure_python       | 175 us                                                          | 167 us: 1.05x faster                                                       |
| xml_etree_generate       | 53.2 ms                                                         | 51.4 ms: 1.03x faster                                                      |
| scimark_monte_carlo      | 39.1 ms                                                         | 38.0 ms: 1.03x faster                                                      |
| pprint_safe_repr         | 474 ms                                                          | 462 ms: 1.03x faster                                                       |
| pickle_list              | 2.90 us                                                         | 2.83 us: 1.03x faster                                                      |
| telco                    | 4.67 ms                                                         | 4.57 ms: 1.02x faster                                                      |
| bench_thread_pool        | 768 us                                                          | 751 us: 1.02x faster                                                       |
| xml_etree_iterparse      | 62.3 ms                                                         | 61.0 ms: 1.02x faster                                                      |
| pickle_dict              | 18.1 us                                                         | 17.8 us: 1.02x faster                                                      |
| xml_etree_process        | 36.4 ms                                                         | 35.9 ms: 1.02x faster                                                      |
| pprint_pformat           | 966 ms                                                          | 956 ms: 1.01x faster                                                       |
| pathlib                  | 75.9 ms                                                         | 75.1 ms: 1.01x faster                                                      |
| comprehensions           | 10.4 us                                                         | 10.3 us: 1.01x faster                                                      |
| coroutines               | 12.8 ms                                                         | 12.7 ms: 1.01x faster                                                      |
| pidigits                 | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| regex_effbot             | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                      |
| regex_dna                | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| json_dumps               | 5.61 ms                                                         | 5.68 ms: 1.01x slower                                                      |
| tornado_http             | 81.8 ms                                                         | 82.9 ms: 1.01x slower                                                      |
| nqueens                  | 56.7 ms                                                         | 57.6 ms: 1.02x slower                                                      |
| html5lib                 | 35.0 ms                                                         | 35.7 ms: 1.02x slower                                                      |
| pickle                   | 7.11 us                                                         | 7.27 us: 1.02x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 980 us: 1.03x slower                                                       |
| unpickle_pure_python     | 122 us                                                          | 125 us: 1.03x slower                                                       |
| async_tree_none          | 218 ms                                                          | 225 ms: 1.03x slower                                                       |
| create_gc_cycles         | 888 us                                                          | 915 us: 1.03x slower                                                       |
| sqlite_synth             | 1.60 us                                                         | 1.65 us: 1.03x slower                                                      |
| async_tree_memoization   | 264 ms                                                          | 272 ms: 1.03x slower                                                       |
| xml_etree_parse          | 90.9 ms                                                         | 94.1 ms: 1.04x slower                                                      |
| logging_silent           | 52.9 ns                                                         | 54.8 ns: 1.04x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 72.8 ms: 1.04x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 781 us: 1.04x slower                                                       |
| raytrace                 | 162 ms                                                          | 170 ms: 1.04x slower                                                       |
| unpickle                 | 8.40 us                                                         | 8.86 us: 1.05x slower                                                      |
| regex_compile            | 78.0 ms                                                         | 82.4 ms: 1.06x slower                                                      |
| generators               | 19.6 ms                                                         | 20.7 ms: 1.06x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.39 sec: 1.06x slower                                                     |
| unpickle_list            | 2.62 us                                                         | 2.78 us: 1.06x slower                                                      |
| go                       | 82.1 ms                                                         | 87.4 ms: 1.07x slower                                                      |
| typing_runtime_protocols | 101 us                                                          | 108 us: 1.07x slower                                                       |
| sympy_sum                | 84.4 ms                                                         | 90.1 ms: 1.07x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                                     |
| sqlglot_optimize         | 32.7 ms                                                         | 35.4 ms: 1.08x slower                                                      |
| coverage                 | 42.1 ms                                                         | 45.6 ms: 1.08x slower                                                      |
| sympy_str                | 159 ms                                                          | 173 ms: 1.09x slower                                                       |
| bench_mp_pool            | 64.8 ms                                                         | 70.6 ms: 1.09x slower                                                      |
| python_startup           | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| async_generators         | 223 ms                                                          | 246 ms: 1.10x slower                                                       |
| scimark_sor              | 75.3 ms                                                         | 83.3 ms: 1.11x slower                                                      |
| sympy_expand             | 271 ms                                                          | 300 ms: 1.11x slower                                                       |
| hexiom                   | 3.72 ms                                                         | 4.13 ms: 1.11x slower                                                      |
| 2to3                     | 207 ms                                                          | 230 ms: 1.11x slower                                                       |
| sympy_integrate          | 12.2 ms                                                         | 13.6 ms: 1.11x slower                                                      |
| pylint                   | 205 ms                                                          | 229 ms: 1.12x slower                                                       |
| django_template          | 21.7 ms                                                         | 24.3 ms: 1.12x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 16.2 ms: 1.12x slower                                                      |
| deltablue                | 1.88 ms                                                         | 2.13 ms: 1.13x slower                                                      |
| richards_super           | 30.2 ms                                                         | 34.8 ms: 1.15x slower                                                      |
| richards                 | 26.7 ms                                                         | 31.0 ms: 1.16x slower                                                      |
| regex_v8                 | 15.8 ms                                                         | 18.5 ms: 1.17x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 39.4 ms: 1.25x slower                                                      |
| scimark_lu               | 56.6 ms                                                         | 72.3 ms: 1.28x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (13): json, async_tree_memoization_tg, async_tree_io_tg, chaos, async_tree_cpu_io_mixed_tg, gc_traversal, json_loads, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl, async_tree_io, asyncio_tcp, pycparser
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 98.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown