# Results vs. 3.13.0b2

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: windows-amd64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.00x slower
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 230 ms: 1.11x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.78 sec: 1.09x slower                                                     |
| html5lib       | 35.0 ms                                                         | 36.8 ms: 1.05x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 86.2 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg        | 605 ms                                                          | 617 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 389 ms                                                          | 400 ms: 1.03x slower                                                       |
| async_tree_none_tg      | 202 ms                                                          | 210 ms: 1.04x slower                                                       |
| async_tree_memoization  | 264 ms                                                          | 277 ms: 1.05x slower                                                       |
| async_tree_none         | 218 ms                                                          | 229 ms: 1.05x slower                                                       |
| Geometric mean          | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 53.1 ms: 1.27x faster                                                      |
| float          | 49.7 ms                                                         | 44.2 ms: 1.13x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                      |
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 88.3 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.21 sec: 1.11x faster                                                     |
| pickle_list          | 2.90 us                                                         | 2.73 us: 1.06x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 51.2 ms: 1.04x faster                                                      |
| pickle_pure_python   | 175 us                                                          | 172 us: 1.02x faster                                                       |
| pickle_dict          | 18.1 us                                                         | 17.8 us: 1.02x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.1 us: 1.01x faster                                                      |
| json_dumps           | 5.61 ms                                                         | 5.75 ms: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.29 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.3 ms: 1.03x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.77 us: 1.04x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 129 us: 1.06x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.82 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.8 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.24 ms: 1.21x faster                                                      |
| django_template | 21.7 ms                                                         | 25.2 ms: 1.16x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.1 ms: 1.26x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 44.6 ms: 1.41x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 508 us: 15.97x faster                                                      |
| spectral_norm            | 63.7 ms                                                         | 44.2 ms: 1.44x faster                                                      |
| nbody                    | 67.6 ms                                                         | 53.1 ms: 1.27x faster                                                      |
| mako                     | 6.36 ms                                                         | 5.24 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.14 ms: 1.17x faster                                                      |
| scimark_fft              | 171 ms                                                          | 150 ms: 1.14x faster                                                       |
| float                    | 49.7 ms                                                         | 44.2 ms: 1.13x faster                                                      |
| fannkuch                 | 243 ms                                                          | 217 ms: 1.12x faster                                                       |
| tomli_loads              | 1.35 sec                                                        | 1.21 sec: 1.11x faster                                                     |
| json                     | 3.19 ms                                                         | 2.90 ms: 1.10x faster                                                      |
| crypto_pyaes             | 45.5 ms                                                         | 41.6 ms: 1.09x faster                                                      |
| regex_v8                 | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                      |
| pyflate                  | 279 ms                                                          | 257 ms: 1.09x faster                                                       |
| pickle_list              | 2.90 us                                                         | 2.73 us: 1.06x faster                                                      |
| deepcopy_memo            | 22.1 us                                                         | 20.9 us: 1.06x faster                                                      |
| asyncio_tcp_ssl          | 1.48 sec                                                        | 1.41 sec: 1.05x faster                                                     |
| xml_etree_generate       | 53.2 ms                                                         | 51.2 ms: 1.04x faster                                                      |
| pprint_safe_repr         | 474 ms                                                          | 457 ms: 1.04x faster                                                       |
| scimark_monte_carlo      | 39.1 ms                                                         | 37.7 ms: 1.04x faster                                                      |
| telco                    | 4.67 ms                                                         | 4.55 ms: 1.03x faster                                                      |
| pickle_pure_python       | 175 us                                                          | 172 us: 1.02x faster                                                       |
| pprint_pformat           | 966 ms                                                          | 949 ms: 1.02x faster                                                       |
| pickle_dict              | 18.1 us                                                         | 17.8 us: 1.02x faster                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                      |
| pathlib                  | 75.9 ms                                                         | 74.9 ms: 1.01x faster                                                      |
| comprehensions           | 10.4 us                                                         | 10.3 us: 1.01x faster                                                      |
| regex_dna                | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| sqlite_synth             | 1.60 us                                                         | 1.59 us: 1.01x faster                                                      |
| json_loads               | 14.2 us                                                         | 14.1 us: 1.01x faster                                                      |
| pidigits                 | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| logging_format           | 6.22 us                                                         | 6.27 us: 1.01x slower                                                      |
| logging_simple           | 5.78 us                                                         | 5.84 us: 1.01x slower                                                      |
| async_tree_io_tg         | 605 ms                                                          | 617 ms: 1.02x slower                                                       |
| create_gc_cycles         | 888 us                                                          | 908 us: 1.02x slower                                                       |
| json_dumps               | 5.61 ms                                                         | 5.75 ms: 1.02x slower                                                      |
| pickle                   | 7.11 us                                                         | 7.29 us: 1.02x slower                                                      |
| async_tree_cpu_io_mixed  | 389 ms                                                          | 400 ms: 1.03x slower                                                       |
| coroutines               | 12.8 ms                                                         | 13.1 ms: 1.03x slower                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 64.3 ms: 1.03x slower                                                      |
| async_tree_none_tg       | 202 ms                                                          | 210 ms: 1.04x slower                                                       |
| unpickle                 | 8.40 us                                                         | 8.77 us: 1.04x slower                                                      |
| chaos                    | 38.4 ms                                                         | 40.1 ms: 1.05x slower                                                      |
| logging_silent           | 52.9 ns                                                         | 55.4 ns: 1.05x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 73.3 ms: 1.05x slower                                                      |
| async_tree_memoization   | 264 ms                                                          | 277 ms: 1.05x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 36.8 ms: 1.05x slower                                                      |
| async_tree_none          | 218 ms                                                          | 229 ms: 1.05x slower                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 2.10 us: 1.05x slower                                                      |
| tornado_http             | 81.8 ms                                                         | 86.2 ms: 1.05x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 809 us: 1.05x slower                                                       |
| unpickle_pure_python     | 122 us                                                          | 129 us: 1.06x slower                                                       |
| nqueens                  | 56.7 ms                                                         | 60.5 ms: 1.07x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 69.3 ms: 1.07x slower                                                      |
| python_startup           | 20.3 ms                                                         | 21.8 ms: 1.07x slower                                                      |
| unpickle_list            | 2.62 us                                                         | 2.82 us: 1.08x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 808 us: 1.08x slower                                                       |
| sqlglot_transpile        | 955 us                                                          | 1.04 ms: 1.09x slower                                                      |
| coverage                 | 42.1 ms                                                         | 45.8 ms: 1.09x slower                                                      |
| deepcopy                 | 220 us                                                          | 239 us: 1.09x slower                                                       |
| docutils                 | 1.63 sec                                                        | 1.78 sec: 1.09x slower                                                     |
| raytrace                 | 162 ms                                                          | 178 ms: 1.10x slower                                                       |
| python_startup_no_site   | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| generators               | 19.6 ms                                                         | 21.6 ms: 1.10x slower                                                      |
| 2to3                     | 207 ms                                                          | 230 ms: 1.11x slower                                                       |
| typing_runtime_protocols | 101 us                                                          | 112 us: 1.11x slower                                                       |
| sympy_sum                | 84.4 ms                                                         | 94.3 ms: 1.12x slower                                                      |
| sympy_str                | 159 ms                                                          | 178 ms: 1.12x slower                                                       |
| richards_super           | 30.2 ms                                                         | 33.8 ms: 1.12x slower                                                      |
| scimark_sor              | 75.3 ms                                                         | 84.7 ms: 1.12x slower                                                      |
| richards                 | 26.7 ms                                                         | 30.1 ms: 1.13x slower                                                      |
| regex_compile            | 78.0 ms                                                         | 88.3 ms: 1.13x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.49 sec: 1.13x slower                                                     |
| async_generators         | 223 ms                                                          | 254 ms: 1.14x slower                                                       |
| sympy_expand             | 271 ms                                                          | 309 ms: 1.14x slower                                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 37.3 ms: 1.14x slower                                                      |
| go                       | 82.1 ms                                                         | 93.8 ms: 1.14x slower                                                      |
| pylint                   | 205 ms                                                          | 235 ms: 1.15x slower                                                       |
| sympy_integrate          | 12.2 ms                                                         | 14.0 ms: 1.15x slower                                                      |
| django_template          | 21.7 ms                                                         | 25.2 ms: 1.16x slower                                                      |
| scimark_lu               | 56.6 ms                                                         | 69.1 ms: 1.22x slower                                                      |
| deltablue                | 1.88 ms                                                         | 2.35 ms: 1.25x slower                                                      |
| hexiom                   | 3.72 ms                                                         | 4.67 ms: 1.26x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 18.1 ms: 1.26x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 44.6 ms: 1.41x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (8): pycparser, asyncio_tcp, xml_etree_process, gc_traversal, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 99.82% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown