
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 18b1fde
- commit date: 2023-07-01
- overall geometric mean: 1.01x faster
- HPT reliability: 91.86%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                     |
| Geometric mean | (ref)                                                       | 1.02x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 153 ms: 1.03x slower                                       |
| float          | 54.6 ms                                                     | 56.8 ms: 1.04x slower                                      |
| nbody          | 70.0 ms                                                     | 75.8 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 92.4 ms: 1.02x slower                                      |
| regex_dna      | 115 ms                                                      | 129 ms: 1.12x slower                                       |
| regex_v8       | 13.8 ms                                                     | 16.3 ms: 1.18x slower                                      |
| regex_effbot   | 1.50 ms                                                     | 1.78 ms: 1.19x slower                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 6.03 ms: 1.25x faster                                      |
| unpickle_pure_python | 152 us                                                      | 141 us: 1.07x faster                                       |
| pickle_pure_python   | 200 us                                                      | 194 us: 1.03x faster                                       |
| xml_etree_parse      | 95.9 ms                                                     | 94.2 ms: 1.02x faster                                      |
| xml_etree_process    | 37.1 ms                                                     | 38.3 ms: 1.03x slower                                      |
| pickle_list          | 2.68 us                                                     | 2.83 us: 1.06x slower                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 66.4 ms: 1.06x slower                                      |
| pickle               | 6.61 us                                                     | 7.10 us: 1.07x slower                                      |
| unpickle             | 8.09 us                                                     | 8.83 us: 1.09x slower                                      |
| xml_etree_generate   | 52.2 ms                                                     | 57.3 ms: 1.10x slower                                      |
| tomli_loads          | 1.41 sec                                                    | 1.56 sec: 1.10x slower                                     |
| json_loads           | 12.9 us                                                     | 14.4 us: 1.12x slower                                      |
| unpickle_list        | 2.55 us                                                     | 2.89 us: 1.13x slower                                      |
| Geometric mean       | (ref)                                                       | 1.03x slower                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 20.2 ms: 1.08x slower                                      |
| python_startup_no_site | 15.9 ms                                                     | 17.3 ms: 1.09x slower                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.81 ms: 1.08x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 94.4 us: 3.41x faster                                      |
| generators               | 33.8 ms                                                     | 23.9 ms: 1.42x faster                                      |
| asyncio_tcp              | 699 ms                                                      | 495 ms: 1.41x faster                                       |
| json_dumps               | 7.56 ms                                                     | 6.03 ms: 1.25x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 37.8 ns: 1.22x faster                                      |
| raytrace                 | 211 ms                                                      | 175 ms: 1.20x faster                                       |
| richards_super           | 37.5 ms                                                     | 32.2 ms: 1.16x faster                                      |
| deltablue                | 2.61 ms                                                     | 2.24 ms: 1.16x faster                                      |
| mdp                      | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                     |
| chaos                    | 47.1 ms                                                     | 41.2 ms: 1.14x faster                                      |
| sqlglot_parse            | 952 us                                                      | 845 us: 1.13x faster                                       |
| coverage                 | 55.9 ms                                                     | 51.3 ms: 1.09x faster                                      |
| sqlglot_transpile        | 1.16 ms                                                     | 1.08 ms: 1.08x faster                                      |
| json                     | 3.25 ms                                                     | 3.03 ms: 1.07x faster                                      |
| unpickle_pure_python     | 152 us                                                      | 141 us: 1.07x faster                                       |
| async_tree_none          | 320 ms                                                      | 299 ms: 1.07x faster                                       |
| richards                 | 30.6 ms                                                     | 28.5 ms: 1.07x faster                                      |
| async_tree_memoization   | 371 ms                                                      | 347 ms: 1.07x faster                                       |
| logging_silent           | 69.8 ns                                                     | 65.5 ns: 1.07x faster                                      |
| comprehensions           | 15.9 us                                                     | 15.1 us: 1.06x faster                                      |
| hexiom                   | 4.55 ms                                                     | 4.32 ms: 1.05x faster                                      |
| go                       | 97.3 ms                                                     | 92.4 ms: 1.05x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 60.5 ms: 1.05x faster                                      |
| async_tree_io            | 779 ms                                                      | 744 ms: 1.05x faster                                       |
| mypy2                    | 229 ms                                                      | 221 ms: 1.04x faster                                       |
| nqueens                  | 64.9 ms                                                     | 62.7 ms: 1.03x faster                                      |
| pickle_pure_python       | 200 us                                                      | 194 us: 1.03x faster                                       |
| sqlglot_normalize        | 190 ms                                                      | 185 ms: 1.03x faster                                       |
| deepcopy                 | 246 us                                                      | 240 us: 1.02x faster                                       |
| xml_etree_parse          | 95.9 ms                                                     | 94.2 ms: 1.02x faster                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 34.4 ms: 1.01x faster                                      |
| deepcopy_memo            | 25.2 us                                                     | 25.0 us: 1.01x faster                                      |
| logging_format           | 7.01 us                                                     | 7.08 us: 1.01x slower                                      |
| crypto_pyaes             | 47.6 ms                                                     | 48.3 ms: 1.02x slower                                      |
| logging_simple           | 6.61 us                                                     | 6.73 us: 1.02x slower                                      |
| meteor_contest           | 74.7 ms                                                     | 76.1 ms: 1.02x slower                                      |
| pyflate                  | 304 ms                                                      | 310 ms: 1.02x slower                                       |
| regex_compile            | 90.6 ms                                                     | 92.4 ms: 1.02x slower                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.63 ms: 1.02x slower                                      |
| spectral_norm            | 67.9 ms                                                     | 69.7 ms: 1.03x slower                                      |
| deepcopy_reduce          | 2.07 us                                                     | 2.13 us: 1.03x slower                                      |
| pidigits                 | 148 ms                                                      | 153 ms: 1.03x slower                                       |
| xml_etree_process        | 37.1 ms                                                     | 38.3 ms: 1.03x slower                                      |
| float                    | 54.6 ms                                                     | 56.8 ms: 1.04x slower                                      |
| docutils                 | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                     |
| coroutines               | 14.6 ms                                                     | 15.3 ms: 1.04x slower                                      |
| pprint_safe_repr         | 512 ms                                                      | 536 ms: 1.05x slower                                       |
| gc_traversal             | 1.46 ms                                                     | 1.53 ms: 1.05x slower                                      |
| dulwich_log              | 44.5 ms                                                     | 46.7 ms: 1.05x slower                                      |
| pprint_pformat           | 1.04 sec                                                    | 1.09 sec: 1.05x slower                                     |
| scimark_fft              | 178 ms                                                      | 188 ms: 1.05x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.83 us: 1.06x slower                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 66.4 ms: 1.06x slower                                      |
| sqlite_synth             | 1.68 us                                                     | 1.80 us: 1.07x slower                                      |
| pickle                   | 6.61 us                                                     | 7.10 us: 1.07x slower                                      |
| mako                     | 7.26 ms                                                     | 7.81 ms: 1.08x slower                                      |
| python_startup           | 18.7 ms                                                     | 20.2 ms: 1.08x slower                                      |
| nbody                    | 70.0 ms                                                     | 75.8 ms: 1.08x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 82.2 ms: 1.09x slower                                      |
| python_startup_no_site   | 15.9 ms                                                     | 17.3 ms: 1.09x slower                                      |
| unpickle                 | 8.09 us                                                     | 8.83 us: 1.09x slower                                      |
| create_gc_cycles         | 693 us                                                      | 759 us: 1.10x slower                                       |
| xml_etree_generate       | 52.2 ms                                                     | 57.3 ms: 1.10x slower                                      |
| bench_mp_pool            | 62.5 ms                                                     | 68.8 ms: 1.10x slower                                      |
| tomli_loads              | 1.41 sec                                                    | 1.56 sec: 1.10x slower                                     |
| json_loads               | 12.9 us                                                     | 14.4 us: 1.12x slower                                      |
| regex_dna                | 115 ms                                                      | 129 ms: 1.12x slower                                       |
| telco                    | 3.90 ms                                                     | 4.40 ms: 1.13x slower                                      |
| unpickle_list            | 2.55 us                                                     | 2.89 us: 1.13x slower                                      |
| pycparser                | 691 ms                                                      | 789 ms: 1.14x slower                                       |
| pathlib                  | 71.4 ms                                                     | 82.8 ms: 1.16x slower                                      |
| regex_v8                 | 13.8 ms                                                     | 16.3 ms: 1.18x slower                                      |
| regex_effbot             | 1.50 ms                                                     | 1.78 ms: 1.19x slower                                      |
| async_generators         | 178 ms                                                      | 241 ms: 1.36x slower                                       |
| Geometric mean           | (ref)                                                       | 1.01x faster                                               |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, scimark_monte_carlo, tornado_http, pickle_dict, fannkuch, asyncio_tcp_ssl, bench_thread_pool
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 91.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
