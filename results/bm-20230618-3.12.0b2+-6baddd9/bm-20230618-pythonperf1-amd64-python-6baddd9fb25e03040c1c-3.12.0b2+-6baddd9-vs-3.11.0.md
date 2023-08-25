
# Results vs. 3.11.0

- fork: python
- ref: 6baddd9fb25e03040c1c
- machine: windows-amd64
- commit hash: 6baddd9
- commit date: 2023-06-18
- overall geometric mean: 1.04x faster
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 219 ms: 1.05x slower                                                        |
| docutils       | 1.60 sec                                                    | 1.65 sec: 1.03x slower                                                      |
| tornado_http   | 91.8 ms                                                     | 89.9 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 68.7 ms: 1.02x faster                                                       |
| pidigits       | 148 ms                                                      | 152 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 86.8 ms: 1.04x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.2 ms: 1.03x slower                                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.08x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.60 ms: 1.35x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 133 us: 1.14x faster                                                        |
| tomli_loads          | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                                      |
| pickle_pure_python   | 200 us                                                      | 194 us: 1.03x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 94.3 ms: 1.02x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 38.0 ms: 1.02x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.9 ms: 1.05x slower                                                       |
| unpickle             | 8.09 us                                                     | 8.55 us: 1.06x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                                       |
| pickle               | 6.61 us                                                     | 7.04 us: 1.07x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.86 us: 1.07x slower                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 56.4 ms: 1.08x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.83 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 17.2 ms: 1.09x slower                                                       |
| python_startup         | 18.7 ms                                                     | 20.4 ms: 1.09x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.96 ms: 1.04x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.4 us: 3.37x faster                                                       |
| generators               | 33.8 ms                                                     | 22.5 ms: 1.50x faster                                                       |
| asyncio_tcp              | 699 ms                                                      | 504 ms: 1.39x faster                                                        |
| json_dumps               | 7.56 ms                                                     | 5.60 ms: 1.35x faster                                                       |
| richards_super           | 37.5 ms                                                     | 29.3 ms: 1.28x faster                                                       |
| deltablue                | 2.61 ms                                                     | 2.06 ms: 1.27x faster                                                       |
| unpack_sequence          | 46.1 ns                                                     | 37.6 ns: 1.22x faster                                                       |
| sqlglot_parse            | 952 us                                                      | 799 us: 1.19x faster                                                        |
| logging_silent           | 69.8 ns                                                     | 59.0 ns: 1.18x faster                                                       |
| richards                 | 30.6 ms                                                     | 26.0 ms: 1.18x faster                                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.00 ms: 1.16x faster                                                       |
| mdp                      | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                      |
| unpickle_pure_python     | 152 us                                                      | 133 us: 1.14x faster                                                        |
| comprehensions           | 15.9 us                                                     | 14.0 us: 1.13x faster                                                       |
| hexiom                   | 4.55 ms                                                     | 4.02 ms: 1.13x faster                                                       |
| raytrace                 | 211 ms                                                      | 187 ms: 1.13x faster                                                        |
| chaos                    | 47.1 ms                                                     | 42.1 ms: 1.12x faster                                                       |
| go                       | 97.3 ms                                                     | 88.7 ms: 1.10x faster                                                       |
| async_tree_none          | 320 ms                                                      | 292 ms: 1.10x faster                                                        |
| json                     | 3.25 ms                                                     | 2.97 ms: 1.10x faster                                                       |
| scimark_lu               | 63.5 ms                                                     | 58.8 ms: 1.08x faster                                                       |
| coverage                 | 55.9 ms                                                     | 52.1 ms: 1.07x faster                                                       |
| async_tree_memoization   | 371 ms                                                      | 346 ms: 1.07x faster                                                        |
| deepcopy_memo            | 25.2 us                                                     | 23.6 us: 1.07x faster                                                       |
| nqueens                  | 64.9 ms                                                     | 61.2 ms: 1.06x faster                                                       |
| mypy2                    | 229 ms                                                      | 217 ms: 1.05x faster                                                        |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.7 ms: 1.05x faster                                                       |
| async_tree_io            | 779 ms                                                      | 745 ms: 1.05x faster                                                        |
| deepcopy                 | 246 us                                                      | 235 us: 1.04x faster                                                        |
| coroutines               | 14.6 ms                                                     | 14.0 ms: 1.04x faster                                                       |
| regex_compile            | 90.6 ms                                                     | 86.8 ms: 1.04x faster                                                       |
| mako                     | 7.26 ms                                                     | 6.96 ms: 1.04x faster                                                       |
| spectral_norm            | 67.9 ms                                                     | 65.2 ms: 1.04x faster                                                       |
| sqlglot_normalize        | 190 ms                                                      | 183 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.48 ms: 1.04x faster                                                       |
| fannkuch                 | 252 ms                                                      | 244 ms: 1.04x faster                                                        |
| sqlglot_optimize         | 34.9 ms                                                     | 33.8 ms: 1.03x faster                                                       |
| tomli_loads              | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                                      |
| pickle_pure_python       | 200 us                                                      | 194 us: 1.03x faster                                                        |
| pyflate                  | 304 ms                                                      | 296 ms: 1.03x faster                                                        |
| tornado_http             | 91.8 ms                                                     | 89.9 ms: 1.02x faster                                                       |
| nbody                    | 70.0 ms                                                     | 68.7 ms: 1.02x faster                                                       |
| xml_etree_parse          | 95.9 ms                                                     | 94.3 ms: 1.02x faster                                                       |
| logging_format           | 7.01 us                                                     | 6.90 us: 1.02x faster                                                       |
| crypto_pyaes             | 47.6 ms                                                     | 46.8 ms: 1.02x faster                                                       |
| dulwich_log              | 44.5 ms                                                     | 43.8 ms: 1.02x faster                                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.03 sec: 1.01x faster                                                      |
| logging_simple           | 6.61 us                                                     | 6.53 us: 1.01x faster                                                       |
| aiohttp                  | 899 us                                                      | 888 us: 1.01x faster                                                        |
| pprint_safe_repr         | 512 ms                                                      | 506 ms: 1.01x faster                                                        |
| meteor_contest           | 74.7 ms                                                     | 74.0 ms: 1.01x faster                                                       |
| xml_etree_process        | 37.1 ms                                                     | 38.0 ms: 1.02x slower                                                       |
| regex_v8                 | 13.8 ms                                                     | 14.2 ms: 1.03x slower                                                       |
| pidigits                 | 148 ms                                                      | 152 ms: 1.03x slower                                                        |
| docutils                 | 1.60 sec                                                    | 1.65 sec: 1.03x slower                                                      |
| gc_traversal             | 1.46 ms                                                     | 1.51 ms: 1.04x slower                                                       |
| 2to3                     | 209 ms                                                      | 219 ms: 1.05x slower                                                        |
| telco                    | 3.90 ms                                                     | 4.10 ms: 1.05x slower                                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.9 ms: 1.05x slower                                                       |
| bench_thread_pool        | 852 us                                                      | 899 us: 1.05x slower                                                        |
| unpickle                 | 8.09 us                                                     | 8.55 us: 1.06x slower                                                       |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                                       |
| pickle                   | 6.61 us                                                     | 7.04 us: 1.07x slower                                                       |
| pickle_list              | 2.68 us                                                     | 2.86 us: 1.07x slower                                                       |
| regex_dna                | 115 ms                                                      | 124 ms: 1.08x slower                                                        |
| regex_effbot             | 1.50 ms                                                     | 1.61 ms: 1.08x slower                                                       |
| xml_etree_generate       | 52.2 ms                                                     | 56.4 ms: 1.08x slower                                                       |
| create_gc_cycles         | 693 us                                                      | 749 us: 1.08x slower                                                        |
| scimark_sor              | 75.6 ms                                                     | 81.7 ms: 1.08x slower                                                       |
| python_startup_no_site   | 15.9 ms                                                     | 17.2 ms: 1.09x slower                                                       |
| python_startup           | 18.7 ms                                                     | 20.4 ms: 1.09x slower                                                       |
| sqlite_synth             | 1.68 us                                                     | 1.85 us: 1.10x slower                                                       |
| unpickle_list            | 2.55 us                                                     | 2.83 us: 1.11x slower                                                       |
| bench_mp_pool            | 62.5 ms                                                     | 69.7 ms: 1.12x slower                                                       |
| pathlib                  | 71.4 ms                                                     | 82.9 ms: 1.16x slower                                                       |
| async_generators         | 178 ms                                                      | 234 ms: 1.32x slower                                                        |
| dask                     | 264 ms                                                      | 371 ms: 1.40x slower                                                        |
| Geometric mean           | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (7): pickle_dict, async_tree_cpu_io_mixed, pycparser, float, scimark_fft, deepcopy_reduce, asyncio_tcp_ssl
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
