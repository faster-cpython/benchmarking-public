
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.76 sec: 1.10x slower                                             |
| Geometric mean | (ref)                                                       | 1.05x slower                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                               |
| float          | 54.6 ms                                                     | 57.6 ms: 1.05x slower                                              |
| nbody          | 70.0 ms                                                     | 79.8 ms: 1.14x slower                                              |
| Geometric mean | (ref)                                                       | 1.07x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                              |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                               |
| regex_compile  | 90.6 ms                                                     | 98.0 ms: 1.08x slower                                              |
| regex_effbot   | 1.50 ms                                                     | 1.68 ms: 1.13x slower                                              |
| Geometric mean | (ref)                                                       | 1.07x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.86 ms: 1.29x faster                                              |
| xml_etree_parse      | 95.9 ms                                                     | 92.7 ms: 1.04x faster                                              |
| unpickle_pure_python | 152 us                                                      | 154 us: 1.02x slower                                               |
| pickle_pure_python   | 200 us                                                      | 204 us: 1.02x slower                                               |
| unpickle             | 8.09 us                                                     | 8.61 us: 1.06x slower                                              |
| pickle               | 6.61 us                                                     | 7.05 us: 1.07x slower                                              |
| pickle_list          | 2.68 us                                                     | 2.88 us: 1.08x slower                                              |
| json_loads           | 12.9 us                                                     | 13.9 us: 1.08x slower                                              |
| xml_etree_iterparse  | 62.6 ms                                                     | 68.0 ms: 1.09x slower                                              |
| xml_etree_process    | 37.1 ms                                                     | 40.4 ms: 1.09x slower                                              |
| xml_etree_generate   | 52.2 ms                                                     | 58.8 ms: 1.13x slower                                              |
| tomli_loads          | 1.41 sec                                                    | 1.64 sec: 1.16x slower                                             |
| unpickle_list        | 2.55 us                                                     | 3.04 us: 1.19x slower                                              |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                       |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 19.4 ms: 1.04x slower                                              |
| python_startup_no_site | 15.9 ms                                                     | 16.7 ms: 1.05x slower                                              |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.39 ms: 1.02x slower                                              |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 98.0 us: 3.28x faster                                              |
| asyncio_tcp              | 699 ms                                                      | 508 ms: 1.37x faster                                               |
| json_dumps               | 7.56 ms                                                     | 5.86 ms: 1.29x faster                                              |
| generators               | 33.8 ms                                                     | 27.0 ms: 1.25x faster                                              |
| unpack_sequence          | 46.1 ns                                                     | 42.0 ns: 1.10x faster                                              |
| raytrace                 | 211 ms                                                      | 195 ms: 1.08x faster                                               |
| deltablue                | 2.61 ms                                                     | 2.42 ms: 1.08x faster                                              |
| json                     | 3.25 ms                                                     | 3.03 ms: 1.07x faster                                              |
| richards_super           | 37.5 ms                                                     | 35.0 ms: 1.07x faster                                              |
| mdp                      | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                             |
| coverage                 | 55.9 ms                                                     | 52.7 ms: 1.06x faster                                              |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.02 sec: 1.05x faster                                             |
| sqlglot_parse            | 952 us                                                      | 912 us: 1.04x faster                                               |
| xml_etree_parse          | 95.9 ms                                                     | 92.7 ms: 1.04x faster                                              |
| logging_silent           | 69.8 ns                                                     | 67.8 ns: 1.03x faster                                              |
| sqlglot_transpile        | 1.16 ms                                                     | 1.15 ms: 1.01x faster                                              |
| bench_thread_pool        | 852 us                                                      | 864 us: 1.01x slower                                               |
| mypy2                    | 229 ms                                                      | 232 ms: 1.01x slower                                               |
| unpickle_pure_python     | 152 us                                                      | 154 us: 1.02x slower                                               |
| mako                     | 7.26 ms                                                     | 7.39 ms: 1.02x slower                                              |
| crypto_pyaes             | 47.6 ms                                                     | 48.4 ms: 1.02x slower                                              |
| regex_v8                 | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 510 ms: 1.02x slower                                               |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                               |
| pickle_pure_python       | 200 us                                                      | 204 us: 1.02x slower                                               |
| scimark_lu               | 63.5 ms                                                     | 65.4 ms: 1.03x slower                                              |
| nqueens                  | 64.9 ms                                                     | 66.9 ms: 1.03x slower                                              |
| richards                 | 30.6 ms                                                     | 31.6 ms: 1.03x slower                                              |
| scimark_monte_carlo      | 44.6 ms                                                     | 46.2 ms: 1.03x slower                                              |
| python_startup           | 18.7 ms                                                     | 19.4 ms: 1.04x slower                                              |
| comprehensions           | 15.9 us                                                     | 16.6 us: 1.04x slower                                              |
| gc_traversal             | 1.46 ms                                                     | 1.53 ms: 1.05x slower                                              |
| python_startup_no_site   | 15.9 ms                                                     | 16.7 ms: 1.05x slower                                              |
| float                    | 54.6 ms                                                     | 57.6 ms: 1.05x slower                                              |
| coroutines               | 14.6 ms                                                     | 15.5 ms: 1.06x slower                                              |
| sqlglot_normalize        | 190 ms                                                      | 201 ms: 1.06x slower                                               |
| logging_simple           | 6.61 us                                                     | 7.01 us: 1.06x slower                                              |
| deepcopy                 | 246 us                                                      | 261 us: 1.06x slower                                               |
| unpickle                 | 8.09 us                                                     | 8.61 us: 1.06x slower                                              |
| deepcopy_memo            | 25.2 us                                                     | 26.8 us: 1.07x slower                                              |
| pickle                   | 6.61 us                                                     | 7.05 us: 1.07x slower                                              |
| sqlglot_optimize         | 34.9 ms                                                     | 37.2 ms: 1.07x slower                                              |
| regex_dna                | 115 ms                                                      | 124 ms: 1.07x slower                                               |
| pickle_list              | 2.68 us                                                     | 2.88 us: 1.08x slower                                              |
| logging_format           | 7.01 us                                                     | 7.54 us: 1.08x slower                                              |
| sqlite_synth             | 1.68 us                                                     | 1.81 us: 1.08x slower                                              |
| dulwich_log              | 44.5 ms                                                     | 48.1 ms: 1.08x slower                                              |
| json_loads               | 12.9 us                                                     | 13.9 us: 1.08x slower                                              |
| regex_compile            | 90.6 ms                                                     | 98.0 ms: 1.08x slower                                              |
| create_gc_cycles         | 693 us                                                      | 751 us: 1.08x slower                                               |
| xml_etree_iterparse      | 62.6 ms                                                     | 68.0 ms: 1.09x slower                                              |
| xml_etree_process        | 37.1 ms                                                     | 40.4 ms: 1.09x slower                                              |
| pprint_pformat           | 1.04 sec                                                    | 1.14 sec: 1.10x slower                                             |
| pprint_safe_repr         | 512 ms                                                      | 561 ms: 1.10x slower                                               |
| meteor_contest           | 74.7 ms                                                     | 82.1 ms: 1.10x slower                                              |
| pyflate                  | 304 ms                                                      | 334 ms: 1.10x slower                                               |
| go                       | 97.3 ms                                                     | 107 ms: 1.10x slower                                               |
| docutils                 | 1.60 sec                                                    | 1.76 sec: 1.10x slower                                             |
| spectral_norm            | 67.9 ms                                                     | 74.9 ms: 1.10x slower                                              |
| hexiom                   | 4.55 ms                                                     | 5.06 ms: 1.11x slower                                              |
| deepcopy_reduce          | 2.07 us                                                     | 2.31 us: 1.11x slower                                              |
| scimark_fft              | 178 ms                                                      | 201 ms: 1.12x slower                                               |
| fannkuch                 | 252 ms                                                      | 284 ms: 1.13x slower                                               |
| regex_effbot             | 1.50 ms                                                     | 1.68 ms: 1.13x slower                                              |
| xml_etree_generate       | 52.2 ms                                                     | 58.8 ms: 1.13x slower                                              |
| pycparser                | 691 ms                                                      | 778 ms: 1.13x slower                                               |
| bench_mp_pool            | 62.5 ms                                                     | 71.1 ms: 1.14x slower                                              |
| nbody                    | 70.0 ms                                                     | 79.8 ms: 1.14x slower                                              |
| tomli_loads              | 1.41 sec                                                    | 1.64 sec: 1.16x slower                                             |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 3.01 ms: 1.17x slower                                              |
| pathlib                  | 71.4 ms                                                     | 84.4 ms: 1.18x slower                                              |
| unpickle_list            | 2.55 us                                                     | 3.04 us: 1.19x slower                                              |
| scimark_sor              | 75.6 ms                                                     | 91.9 ms: 1.22x slower                                              |
| telco                    | 3.90 ms                                                     | 4.88 ms: 1.25x slower                                              |
| async_generators         | 178 ms                                                      | 252 ms: 1.42x slower                                               |
| dask                     | 264 ms                                                      | 398 ms: 1.51x slower                                               |
| Geometric mean           | (ref)                                                       | 1.03x slower                                                       |

Benchmark hidden because not significant (6): async_tree_io, async_tree_memoization, async_tree_none, tornado_http, pickle_dict, chaos
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x
