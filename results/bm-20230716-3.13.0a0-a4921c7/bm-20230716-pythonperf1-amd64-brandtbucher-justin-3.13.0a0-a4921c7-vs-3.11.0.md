
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.02x faster
- HPT reliability: 75.38%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.64 sec: 1.02x slower                                             |
| tornado_http   | 91.8 ms                                                     | 89.6 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                       | 1.00x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 52.0 ms: 1.05x faster                                              |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                               |
| nbody          | 70.0 ms                                                     | 72.1 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                       | 1.00x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 88.7 ms: 1.02x faster                                              |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                               |
| regex_effbot   | 1.50 ms                                                     | 1.56 ms: 1.04x slower                                              |
| regex_v8       | 13.8 ms                                                     | 24.0 ms: 1.73x slower                                              |
| Geometric mean | (ref)                                                       | 1.16x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.78 ms: 1.31x faster                                              |
| unpickle_pure_python | 152 us                                                      | 136 us: 1.11x faster                                               |
| xml_etree_parse      | 95.9 ms                                                     | 92.8 ms: 1.03x faster                                              |
| pickle_pure_python   | 200 us                                                      | 196 us: 1.02x faster                                               |
| unpickle             | 8.09 us                                                     | 8.26 us: 1.02x slower                                              |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.0 ms: 1.02x slower                                              |
| pickle_dict          | 18.5 us                                                     | 19.1 us: 1.03x slower                                              |
| json_loads           | 12.9 us                                                     | 13.5 us: 1.05x slower                                              |
| xml_etree_process    | 37.1 ms                                                     | 39.2 ms: 1.06x slower                                              |
| pickle               | 6.61 us                                                     | 7.15 us: 1.08x slower                                              |
| xml_etree_generate   | 52.2 ms                                                     | 56.8 ms: 1.09x slower                                              |
| pickle_list          | 2.68 us                                                     | 2.92 us: 1.09x slower                                              |
| unpickle_list        | 2.55 us                                                     | 2.84 us: 1.12x slower                                              |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 22.2 ms: 1.19x slower                                              |
| python_startup_no_site | 15.9 ms                                                     | 19.3 ms: 1.22x slower                                              |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.39 ms: 1.02x slower                                              |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 97.3 us: 3.31x faster                                              |
| asyncio_tcp              | 699 ms                                                      | 478 ms: 1.46x faster                                               |
| generators               | 33.8 ms                                                     | 23.9 ms: 1.41x faster                                              |
| json_dumps               | 7.56 ms                                                     | 5.78 ms: 1.31x faster                                              |
| richards_super           | 37.5 ms                                                     | 30.1 ms: 1.25x faster                                              |
| unpack_sequence          | 46.1 ns                                                     | 37.8 ns: 1.22x faster                                              |
| mdp                      | 1.67 sec                                                    | 1.40 sec: 1.20x faster                                             |
| richards                 | 30.6 ms                                                     | 26.5 ms: 1.15x faster                                              |
| json                     | 3.25 ms                                                     | 2.87 ms: 1.13x faster                                              |
| sqlglot_parse            | 952 us                                                      | 842 us: 1.13x faster                                               |
| deltablue                | 2.61 ms                                                     | 2.31 ms: 1.13x faster                                              |
| unpickle_pure_python     | 152 us                                                      | 136 us: 1.11x faster                                               |
| logging_silent           | 69.8 ns                                                     | 62.9 ns: 1.11x faster                                              |
| sqlglot_transpile        | 1.16 ms                                                     | 1.06 ms: 1.10x faster                                              |
| async_tree_none          | 320 ms                                                      | 294 ms: 1.09x faster                                               |
| async_tree_memoization   | 371 ms                                                      | 344 ms: 1.08x faster                                               |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.97 sec: 1.07x faster                                             |
| raytrace                 | 211 ms                                                      | 197 ms: 1.07x faster                                               |
| mypy2                    | 229 ms                                                      | 215 ms: 1.07x faster                                               |
| chaos                    | 47.1 ms                                                     | 44.2 ms: 1.07x faster                                              |
| go                       | 97.3 ms                                                     | 91.4 ms: 1.07x faster                                              |
| async_tree_io            | 779 ms                                                      | 735 ms: 1.06x faster                                               |
| float                    | 54.6 ms                                                     | 52.0 ms: 1.05x faster                                              |
| coverage                 | 55.9 ms                                                     | 53.3 ms: 1.05x faster                                              |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.8 ms: 1.04x faster                                              |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 481 ms: 1.04x faster                                               |
| dulwich_log              | 44.5 ms                                                     | 42.9 ms: 1.04x faster                                              |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.48 ms: 1.04x faster                                              |
| xml_etree_parse          | 95.9 ms                                                     | 92.8 ms: 1.03x faster                                              |
| spectral_norm            | 67.9 ms                                                     | 66.0 ms: 1.03x faster                                              |
| tornado_http             | 91.8 ms                                                     | 89.6 ms: 1.03x faster                                              |
| comprehensions           | 15.9 us                                                     | 15.5 us: 1.02x faster                                              |
| bench_thread_pool        | 852 us                                                      | 832 us: 1.02x faster                                               |
| regex_compile            | 90.6 ms                                                     | 88.7 ms: 1.02x faster                                              |
| deepcopy                 | 246 us                                                      | 240 us: 1.02x faster                                               |
| pickle_pure_python       | 200 us                                                      | 196 us: 1.02x faster                                               |
| nqueens                  | 64.9 ms                                                     | 63.9 ms: 1.02x faster                                              |
| sqlglot_normalize        | 190 ms                                                      | 188 ms: 1.01x faster                                               |
| pyflate                  | 304 ms                                                      | 301 ms: 1.01x faster                                               |
| logging_simple           | 6.61 us                                                     | 6.58 us: 1.01x faster                                              |
| regex_dna                | 115 ms                                                      | 116 ms: 1.01x slower                                               |
| meteor_contest           | 74.7 ms                                                     | 75.4 ms: 1.01x slower                                              |
| coroutines               | 14.6 ms                                                     | 14.8 ms: 1.01x slower                                              |
| fannkuch                 | 252 ms                                                      | 255 ms: 1.01x slower                                               |
| hexiom                   | 4.55 ms                                                     | 4.62 ms: 1.01x slower                                              |
| scimark_fft              | 178 ms                                                      | 181 ms: 1.01x slower                                               |
| pprint_safe_repr         | 512 ms                                                      | 520 ms: 1.02x slower                                               |
| gc_traversal             | 1.46 ms                                                     | 1.48 ms: 1.02x slower                                              |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                               |
| mako                     | 7.26 ms                                                     | 7.39 ms: 1.02x slower                                              |
| deepcopy_reduce          | 2.07 us                                                     | 2.11 us: 1.02x slower                                              |
| unpickle                 | 8.09 us                                                     | 8.26 us: 1.02x slower                                              |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.0 ms: 1.02x slower                                              |
| docutils                 | 1.60 sec                                                    | 1.64 sec: 1.02x slower                                             |
| pprint_pformat           | 1.04 sec                                                    | 1.06 sec: 1.02x slower                                             |
| nbody                    | 70.0 ms                                                     | 72.1 ms: 1.03x slower                                              |
| pickle_dict              | 18.5 us                                                     | 19.1 us: 1.03x slower                                              |
| sqlite_synth             | 1.68 us                                                     | 1.74 us: 1.03x slower                                              |
| create_gc_cycles         | 693 us                                                      | 722 us: 1.04x slower                                               |
| regex_effbot             | 1.50 ms                                                     | 1.56 ms: 1.04x slower                                              |
| json_loads               | 12.9 us                                                     | 13.5 us: 1.05x slower                                              |
| telco                    | 3.90 ms                                                     | 4.11 ms: 1.05x slower                                              |
| scimark_sor              | 75.6 ms                                                     | 79.6 ms: 1.05x slower                                              |
| xml_etree_process        | 37.1 ms                                                     | 39.2 ms: 1.06x slower                                              |
| deepcopy_memo            | 25.2 us                                                     | 27.2 us: 1.08x slower                                              |
| pickle                   | 6.61 us                                                     | 7.15 us: 1.08x slower                                              |
| xml_etree_generate       | 52.2 ms                                                     | 56.8 ms: 1.09x slower                                              |
| pickle_list              | 2.68 us                                                     | 2.92 us: 1.09x slower                                              |
| scimark_lu               | 63.5 ms                                                     | 70.3 ms: 1.11x slower                                              |
| unpickle_list            | 2.55 us                                                     | 2.84 us: 1.12x slower                                              |
| bench_mp_pool            | 62.5 ms                                                     | 70.0 ms: 1.12x slower                                              |
| pathlib                  | 71.4 ms                                                     | 80.3 ms: 1.13x slower                                              |
| crypto_pyaes             | 47.6 ms                                                     | 53.6 ms: 1.13x slower                                              |
| python_startup           | 18.7 ms                                                     | 22.2 ms: 1.19x slower                                              |
| python_startup_no_site   | 15.9 ms                                                     | 19.3 ms: 1.22x slower                                              |
| async_generators         | 178 ms                                                      | 239 ms: 1.35x slower                                               |
| dask                     | 264 ms                                                      | 363 ms: 1.38x slower                                               |
| regex_v8                 | 13.8 ms                                                     | 24.0 ms: 1.73x slower                                              |
| Geometric mean           | (ref)                                                       | 1.02x faster                                                       |

Benchmark hidden because not significant (4): pycparser, sqlglot_optimize, logging_format, tomli_loads
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 75.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
