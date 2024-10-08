# Results vs. 3.13.0b2

- fork: python
- ref: 363374cf69a7e2292fe3
- machine: windows-amd64
- commit hash: 363374c
- commit date: 2024-08-10
- overall geometric mean: 1.01x slower
- HPT reliability: 99.57%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 240 ms: 1.16x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.85 sec: 1.14x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 96.1 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.17x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg | 605 ms                                                          | 547 ms: 1.11x faster                                                       |
| Geometric mean   | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 50.0 ms: 1.35x faster                                                      |
| float          | 49.7 ms                                                         | 44.3 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                           | 1.15x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| regex_dna      | 119 ms                                                          | 124 ms: 1.05x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 90.0 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.27 sec: 1.06x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 52.9 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 182 us: 1.04x slower                                                       |
| xml_etree_process    | 36.4 ms                                                         | 38.0 ms: 1.04x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 94.9 ms: 1.04x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.94 ms: 1.06x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 134 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.10x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.08 ms: 1.25x faster                                                      |
| django_template | 21.7 ms                                                         | 25.1 ms: 1.16x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.5 ms: 1.22x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 38.6 ms: 1.22x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.08x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 515 us: 15.74x faster                                                      |
| spectral_norm            | 63.7 ms                                                         | 46.7 ms: 1.36x faster                                                      |
| nbody                    | 67.6 ms                                                         | 50.0 ms: 1.35x faster                                                      |
| deepcopy_memo            | 22.1 us                                                         | 16.3 us: 1.35x faster                                                      |
| mako                     | 6.36 ms                                                         | 5.08 ms: 1.25x faster                                                      |
| scimark_sor              | 75.3 ms                                                         | 61.5 ms: 1.23x faster                                                      |
| deepcopy                 | 220 us                                                          | 184 us: 1.20x faster                                                       |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.13 ms: 1.17x faster                                                      |
| scimark_fft              | 171 ms                                                          | 149 ms: 1.14x faster                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 40.0 ms: 1.14x faster                                                      |
| pyflate                  | 279 ms                                                          | 248 ms: 1.12x faster                                                       |
| fannkuch                 | 243 ms                                                          | 217 ms: 1.12x faster                                                       |
| float                    | 49.7 ms                                                         | 44.3 ms: 1.12x faster                                                      |
| async_tree_io_tg         | 605 ms                                                          | 547 ms: 1.11x faster                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 1.81 us: 1.10x faster                                                      |
| asyncio_tcp_ssl          | 1.48 sec                                                        | 1.39 sec: 1.07x faster                                                     |
| tomli_loads              | 1.35 sec                                                        | 1.27 sec: 1.06x faster                                                     |
| scimark_monte_carlo      | 39.1 ms                                                         | 37.7 ms: 1.04x faster                                                      |
| scimark_lu               | 56.6 ms                                                         | 55.3 ms: 1.02x faster                                                      |
| telco                    | 4.67 ms                                                         | 4.59 ms: 1.02x faster                                                      |
| comprehensions           | 10.4 us                                                         | 10.2 us: 1.01x faster                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 52.9 ms: 1.01x faster                                                      |
| pprint_pformat           | 966 ms                                                          | 975 ms: 1.01x slower                                                       |
| json_loads               | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| gc_traversal             | 1.55 ms                                                         | 1.59 ms: 1.02x slower                                                      |
| chaos                    | 38.4 ms                                                         | 39.3 ms: 1.02x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 71.7 ms: 1.03x slower                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| logging_simple           | 5.78 us                                                         | 6.01 us: 1.04x slower                                                      |
| pickle_pure_python       | 175 us                                                          | 182 us: 1.04x slower                                                       |
| logging_format           | 6.22 us                                                         | 6.48 us: 1.04x slower                                                      |
| xml_etree_process        | 36.4 ms                                                         | 38.0 ms: 1.04x slower                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 94.9 ms: 1.04x slower                                                      |
| create_gc_cycles         | 888 us                                                          | 927 us: 1.04x slower                                                       |
| regex_dna                | 119 ms                                                          | 124 ms: 1.05x slower                                                       |
| json_dumps               | 5.61 ms                                                         | 5.94 ms: 1.06x slower                                                      |
| logging_silent           | 52.9 ns                                                         | 56.5 ns: 1.07x slower                                                      |
| pathlib                  | 75.9 ms                                                         | 81.6 ms: 1.08x slower                                                      |
| generators               | 19.6 ms                                                         | 21.2 ms: 1.08x slower                                                      |
| coroutines               | 12.8 ms                                                         | 13.8 ms: 1.09x slower                                                      |
| nqueens                  | 56.7 ms                                                         | 61.6 ms: 1.09x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 836 us: 1.09x slower                                                       |
| python_startup           | 20.3 ms                                                         | 22.2 ms: 1.10x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                                     |
| unpickle_pure_python     | 122 us                                                          | 134 us: 1.10x slower                                                       |
| sqlglot_normalize        | 173 ms                                                          | 191 ms: 1.10x slower                                                       |
| sqlglot_parse            | 748 us                                                          | 828 us: 1.11x slower                                                       |
| coverage                 | 42.1 ms                                                         | 46.8 ms: 1.11x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 1.06 ms: 1.11x slower                                                      |
| dulwich_log              | 38.0 ms                                                         | 42.9 ms: 1.13x slower                                                      |
| pycparser                | 754 ms                                                          | 851 ms: 1.13x slower                                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 37.0 ms: 1.13x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 18.4 ms: 1.13x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 73.4 ms: 1.13x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.85 sec: 1.14x slower                                                     |
| sympy_sum                | 84.4 ms                                                         | 96.9 ms: 1.15x slower                                                      |
| regex_compile            | 78.0 ms                                                         | 90.0 ms: 1.15x slower                                                      |
| typing_runtime_protocols | 101 us                                                          | 117 us: 1.16x slower                                                       |
| django_template          | 21.7 ms                                                         | 25.1 ms: 1.16x slower                                                      |
| 2to3                     | 207 ms                                                          | 240 ms: 1.16x slower                                                       |
| richards                 | 26.7 ms                                                         | 31.1 ms: 1.16x slower                                                      |
| async_generators         | 223 ms                                                          | 260 ms: 1.16x slower                                                       |
| asyncio_tcp              | 471 ms                                                          | 550 ms: 1.17x slower                                                       |
| richards_super           | 30.2 ms                                                         | 35.2 ms: 1.17x slower                                                      |
| tornado_http             | 81.8 ms                                                         | 96.1 ms: 1.17x slower                                                      |
| sympy_str                | 159 ms                                                          | 188 ms: 1.18x slower                                                       |
| raytrace                 | 162 ms                                                          | 194 ms: 1.19x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| sympy_integrate          | 12.2 ms                                                         | 14.7 ms: 1.20x slower                                                      |
| sympy_expand             | 271 ms                                                          | 330 ms: 1.22x slower                                                       |
| genshi_text              | 14.4 ms                                                         | 17.5 ms: 1.22x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 38.6 ms: 1.22x slower                                                      |
| go                       | 82.1 ms                                                         | 100 ms: 1.22x slower                                                       |
| deltablue                | 1.88 ms                                                         | 2.34 ms: 1.24x slower                                                      |
| pylint                   | 205 ms                                                          | 255 ms: 1.25x slower                                                       |
| hexiom                   | 3.72 ms                                                         | 4.75 ms: 1.27x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (12): async_tree_none_tg, async_tree_memoization_tg, async_tree_io, regex_v8, json, async_tree_none, async_tree_cpu_io_mixed_tg, xml_etree_iterparse, async_tree_memoization, pprint_safe_repr, pidigits, async_tree_cpu_io_mixed
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.57% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown