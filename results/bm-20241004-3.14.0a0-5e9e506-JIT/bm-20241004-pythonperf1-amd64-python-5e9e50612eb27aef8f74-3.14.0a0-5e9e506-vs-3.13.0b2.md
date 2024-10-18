# Results vs. 3.13.0b2

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: windows-amd64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.05x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 253 ms: 1.22x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.95 sec: 1.20x slower                                                     |
| html5lib       | 35.0 ms                                                         | 41.7 ms: 1.19x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 98.2 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                           | 1.20x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 574 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 401 ms: 1.05x slower                                                       |
| async_tree_memoization     | 264 ms                                                          | 282 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (5): async_tree_io, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 49.4 ms: 1.37x faster                                                      |
| float          | 49.7 ms                                                         | 47.2 ms: 1.05x faster                                                      |
| pidigits       | 150 ms                                                          | 147 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                           | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 117 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 95.7 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list          | 2.90 us                                                         | 2.72 us: 1.07x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 50.5 ms: 1.05x faster                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.30 sec: 1.04x faster                                                     |
| pickle_dict          | 18.1 us                                                         | 17.8 us: 1.02x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 63.0 ms: 1.01x slower                                                      |
| pickle               | 7.11 us                                                         | 7.24 us: 1.02x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.84 ms: 1.04x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 95.8 ms: 1.05x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.94 us: 1.06x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.83 us: 1.08x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 198 us: 1.13x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 147 us: 1.21x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 18.5 ms: 1.14x slower                                                      |
| python_startup         | 20.3 ms                                                         | 24.3 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.17x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 4.99 ms: 1.27x faster                                                      |
| django_template | 21.7 ms                                                         | 26.9 ms: 1.24x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 19.1 ms: 1.33x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 47.3 ms: 1.50x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.18x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 523 us: 15.49x faster                                                      |
| nbody                      | 67.6 ms                                                         | 49.4 ms: 1.37x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 16.2 us: 1.36x faster                                                      |
| mako                       | 6.36 ms                                                         | 4.99 ms: 1.27x faster                                                      |
| scimark_sor                | 75.3 ms                                                         | 61.9 ms: 1.22x faster                                                      |
| spectral_norm              | 63.7 ms                                                         | 52.6 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.11 ms: 1.19x faster                                                      |
| deepcopy                   | 220 us                                                          | 186 us: 1.18x faster                                                       |
| crypto_pyaes               | 45.5 ms                                                         | 40.6 ms: 1.12x faster                                                      |
| scimark_fft                | 171 ms                                                          | 153 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.81 us: 1.10x faster                                                      |
| pickle_list                | 2.90 us                                                         | 2.72 us: 1.07x faster                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 36.6 ms: 1.07x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 574 ms: 1.05x faster                                                       |
| float                      | 49.7 ms                                                         | 47.2 ms: 1.05x faster                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 50.5 ms: 1.05x faster                                                      |
| pprint_safe_repr           | 474 ms                                                          | 450 ms: 1.05x faster                                                       |
| telco                      | 4.67 ms                                                         | 4.46 ms: 1.05x faster                                                      |
| pprint_pformat             | 966 ms                                                          | 923 ms: 1.05x faster                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.30 sec: 1.04x faster                                                     |
| pickle_dict                | 18.1 us                                                         | 17.8 us: 1.02x faster                                                      |
| pidigits                   | 150 ms                                                          | 147 ms: 1.02x faster                                                       |
| scimark_lu                 | 56.6 ms                                                         | 55.7 ms: 1.02x faster                                                      |
| regex_dna                  | 119 ms                                                          | 117 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.60 us                                                         | 1.59 us: 1.01x faster                                                      |
| json_loads                 | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 63.0 ms: 1.01x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.24 us: 1.02x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 5.84 ms: 1.04x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.54 sec: 1.04x slower                                                     |
| fannkuch                   | 243 ms                                                          | 254 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 401 ms: 1.05x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 95.8 ms: 1.05x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.15 us: 1.06x slower                                                      |
| unpickle                   | 8.40 us                                                         | 8.94 us: 1.06x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.63 us: 1.07x slower                                                      |
| async_tree_memoization     | 264 ms                                                          | 282 ms: 1.07x slower                                                       |
| pathlib                    | 75.9 ms                                                         | 81.3 ms: 1.07x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 75.4 ms: 1.08x slower                                                      |
| chaos                      | 38.4 ms                                                         | 41.5 ms: 1.08x slower                                                      |
| unpickle_list              | 2.62 us                                                         | 2.83 us: 1.08x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 843 us: 1.10x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 111 us: 1.10x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 58.2 ns: 1.10x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.1 ms: 1.11x slower                                                      |
| pyflate                    | 279 ms                                                          | 310 ms: 1.11x slower                                                       |
| comprehensions             | 10.4 us                                                         | 11.6 us: 1.12x slower                                                      |
| go                         | 82.1 ms                                                         | 91.9 ms: 1.12x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 198 us: 1.13x slower                                                       |
| dulwich_log                | 38.0 ms                                                         | 43.2 ms: 1.14x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.5 ms: 1.14x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 65.1 ms: 1.15x slower                                                      |
| async_generators           | 223 ms                                                          | 260 ms: 1.16x slower                                                       |
| coverage                   | 42.1 ms                                                         | 49.6 ms: 1.18x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 205 ms: 1.18x slower                                                       |
| generators                 | 19.6 ms                                                         | 23.2 ms: 1.18x slower                                                      |
| sqlglot_parse              | 748 us                                                          | 887 us: 1.19x slower                                                       |
| html5lib                   | 35.0 ms                                                         | 41.7 ms: 1.19x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.95 sec: 1.20x slower                                                     |
| python_startup             | 20.3 ms                                                         | 24.3 ms: 1.20x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 98.2 ms: 1.20x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 147 us: 1.21x slower                                                       |
| 2to3                       | 207 ms                                                          | 253 ms: 1.22x slower                                                       |
| regex_compile              | 78.0 ms                                                         | 95.7 ms: 1.23x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.61 sec: 1.23x slower                                                     |
| sqlglot_transpile          | 955 us                                                          | 1.17 ms: 1.23x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 104 ms: 1.23x slower                                                       |
| sympy_str                  | 159 ms                                                          | 196 ms: 1.23x slower                                                       |
| sympy_expand               | 271 ms                                                          | 334 ms: 1.23x slower                                                       |
| django_template            | 21.7 ms                                                         | 26.9 ms: 1.24x slower                                                      |
| deltablue                  | 1.88 ms                                                         | 2.34 ms: 1.24x slower                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.93 ms: 1.24x slower                                                      |
| raytrace                   | 162 ms                                                          | 202 ms: 1.25x slower                                                       |
| sympy_integrate            | 12.2 ms                                                         | 15.6 ms: 1.27x slower                                                      |
| richards_super             | 30.2 ms                                                         | 38.6 ms: 1.28x slower                                                      |
| richards                   | 26.7 ms                                                         | 34.5 ms: 1.29x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 42.9 ms: 1.31x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 19.1 ms: 1.33x slower                                                      |
| pylint                     | 205 ms                                                          | 279 ms: 1.37x slower                                                       |
| bench_mp_pool              | 64.8 ms                                                         | 88.9 ms: 1.37x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 5.28 ms: 1.42x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 673 ms: 1.43x slower                                                       |
| genshi_xml                 | 31.6 ms                                                         | 47.3 ms: 1.50x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 1.38 ms: 1.56x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (10): regex_v8, async_tree_io, json, async_tree_cpu_io_mixed, async_tree_none, regex_effbot, async_tree_none_tg, xml_etree_process, pycparser, async_tree_memoization_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (2) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown