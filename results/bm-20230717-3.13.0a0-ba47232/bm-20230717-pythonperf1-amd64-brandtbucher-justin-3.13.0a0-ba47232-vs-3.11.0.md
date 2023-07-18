
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: ba47232
- commit date: 2023-07-17
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                             |
| tornado_http   | 91.8 ms                                                     | 88.6 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                       | 1.01x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 50.5 ms: 1.08x faster                                              |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                               |
| nbody          | 70.0 ms                                                     | 72.3 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                       | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 88.6 ms: 1.02x faster                                              |
| regex_effbot   | 1.50 ms                                                     | 1.63 ms: 1.09x slower                                              |
| regex_dna      | 115 ms                                                      | 126 ms: 1.09x slower                                               |
| regex_v8       | 13.8 ms                                                     | 26.0 ms: 1.88x slower                                              |
| Geometric mean | (ref)                                                       | 1.22x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.67 ms: 1.33x faster                                              |
| unpickle_pure_python | 152 us                                                      | 137 us: 1.11x faster                                               |
| tomli_loads          | 1.41 sec                                                    | 1.36 sec: 1.04x faster                                             |
| xml_etree_parse      | 95.9 ms                                                     | 92.5 ms: 1.04x faster                                              |
| pickle_pure_python   | 200 us                                                      | 197 us: 1.01x faster                                               |
| unpickle             | 8.09 us                                                     | 8.30 us: 1.03x slower                                              |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.6 ms: 1.03x slower                                              |
| xml_etree_process    | 37.1 ms                                                     | 38.4 ms: 1.04x slower                                              |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                              |
| xml_etree_generate   | 52.2 ms                                                     | 55.4 ms: 1.06x slower                                              |
| pickle_list          | 2.68 us                                                     | 2.87 us: 1.07x slower                                              |
| pickle               | 6.61 us                                                     | 7.20 us: 1.09x slower                                              |
| unpickle_list        | 2.55 us                                                     | 2.89 us: 1.14x slower                                              |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                       |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 21.1 ms: 1.13x slower                                              |
| python_startup_no_site | 15.9 ms                                                     | 18.1 ms: 1.14x slower                                              |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.42 ms: 1.13x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 97.8 us: 3.29x faster                                              |
| generators               | 33.8 ms                                                     | 23.0 ms: 1.47x faster                                              |
| asyncio_tcp              | 699 ms                                                      | 476 ms: 1.47x faster                                               |
| json_dumps               | 7.56 ms                                                     | 5.67 ms: 1.33x faster                                              |
| richards_super           | 37.5 ms                                                     | 29.6 ms: 1.27x faster                                              |
| unpack_sequence          | 46.1 ns                                                     | 37.4 ns: 1.23x faster                                              |
| deltablue                | 2.61 ms                                                     | 2.12 ms: 1.23x faster                                              |
| richards                 | 30.6 ms                                                     | 26.1 ms: 1.17x faster                                              |
| sqlglot_parse            | 952 us                                                      | 821 us: 1.16x faster                                               |
| mako                     | 7.26 ms                                                     | 6.42 ms: 1.13x faster                                              |
| json                     | 3.25 ms                                                     | 2.88 ms: 1.13x faster                                              |
| logging_silent           | 69.8 ns                                                     | 61.8 ns: 1.13x faster                                              |
| sqlglot_transpile        | 1.16 ms                                                     | 1.04 ms: 1.12x faster                                              |
| scimark_lu               | 63.5 ms                                                     | 56.8 ms: 1.12x faster                                              |
| comprehensions           | 15.9 us                                                     | 14.3 us: 1.11x faster                                              |
| mdp                      | 1.67 sec                                                    | 1.51 sec: 1.11x faster                                             |
| unpickle_pure_python     | 152 us                                                      | 137 us: 1.11x faster                                               |
| coverage                 | 55.9 ms                                                     | 50.8 ms: 1.10x faster                                              |
| go                       | 97.3 ms                                                     | 88.5 ms: 1.10x faster                                              |
| async_tree_none          | 320 ms                                                      | 293 ms: 1.09x faster                                               |
| raytrace                 | 211 ms                                                      | 195 ms: 1.08x faster                                               |
| float                    | 54.6 ms                                                     | 50.5 ms: 1.08x faster                                              |
| async_tree_memoization   | 371 ms                                                      | 344 ms: 1.08x faster                                               |
| deepcopy_memo            | 25.2 us                                                     | 23.5 us: 1.07x faster                                              |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.97 sec: 1.07x faster                                             |
| chaos                    | 47.1 ms                                                     | 44.1 ms: 1.07x faster                                              |
| mypy2                    | 229 ms                                                      | 215 ms: 1.07x faster                                               |
| pyflate                  | 304 ms                                                      | 286 ms: 1.06x faster                                               |
| async_tree_io            | 779 ms                                                      | 733 ms: 1.06x faster                                               |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 481 ms: 1.04x faster                                               |
| tomli_loads              | 1.41 sec                                                    | 1.36 sec: 1.04x faster                                             |
| tornado_http             | 91.8 ms                                                     | 88.6 ms: 1.04x faster                                              |
| xml_etree_parse          | 95.9 ms                                                     | 92.5 ms: 1.04x faster                                              |
| spectral_norm            | 67.9 ms                                                     | 65.5 ms: 1.04x faster                                              |
| nqueens                  | 64.9 ms                                                     | 62.7 ms: 1.03x faster                                              |
| hexiom                   | 4.55 ms                                                     | 4.41 ms: 1.03x faster                                              |
| fannkuch                 | 252 ms                                                      | 245 ms: 1.03x faster                                               |
| scimark_monte_carlo      | 44.6 ms                                                     | 43.4 ms: 1.03x faster                                              |
| bench_thread_pool        | 852 us                                                      | 829 us: 1.03x faster                                               |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.51 ms: 1.03x faster                                              |
| logging_simple           | 6.61 us                                                     | 6.46 us: 1.02x faster                                              |
| regex_compile            | 90.6 ms                                                     | 88.6 ms: 1.02x faster                                              |
| dulwich_log              | 44.5 ms                                                     | 43.6 ms: 1.02x faster                                              |
| deepcopy                 | 246 us                                                      | 241 us: 1.02x faster                                               |
| sqlglot_normalize        | 190 ms                                                      | 187 ms: 1.02x faster                                               |
| logging_format           | 7.01 us                                                     | 6.90 us: 1.02x faster                                              |
| pickle_pure_python       | 200 us                                                      | 197 us: 1.01x faster                                               |
| pycparser                | 691 ms                                                      | 683 ms: 1.01x faster                                               |
| sqlglot_optimize         | 34.9 ms                                                     | 34.5 ms: 1.01x faster                                              |
| pprint_safe_repr         | 512 ms                                                      | 509 ms: 1.01x faster                                               |
| meteor_contest           | 74.7 ms                                                     | 75.1 ms: 1.00x slower                                              |
| gc_traversal             | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                              |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                               |
| docutils                 | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                             |
| scimark_fft              | 178 ms                                                      | 181 ms: 1.01x slower                                               |
| sqlite_synth             | 1.68 us                                                     | 1.72 us: 1.02x slower                                              |
| unpickle                 | 8.09 us                                                     | 8.30 us: 1.03x slower                                              |
| telco                    | 3.90 ms                                                     | 4.02 ms: 1.03x slower                                              |
| create_gc_cycles         | 693 us                                                      | 714 us: 1.03x slower                                               |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.6 ms: 1.03x slower                                              |
| nbody                    | 70.0 ms                                                     | 72.3 ms: 1.03x slower                                              |
| xml_etree_process        | 37.1 ms                                                     | 38.4 ms: 1.04x slower                                              |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                              |
| xml_etree_generate       | 52.2 ms                                                     | 55.4 ms: 1.06x slower                                              |
| crypto_pyaes             | 47.6 ms                                                     | 50.5 ms: 1.06x slower                                              |
| pickle_list              | 2.68 us                                                     | 2.87 us: 1.07x slower                                              |
| regex_effbot             | 1.50 ms                                                     | 1.63 ms: 1.09x slower                                              |
| scimark_sor              | 75.6 ms                                                     | 82.3 ms: 1.09x slower                                              |
| pickle                   | 6.61 us                                                     | 7.20 us: 1.09x slower                                              |
| regex_dna                | 115 ms                                                      | 126 ms: 1.09x slower                                               |
| pathlib                  | 71.4 ms                                                     | 79.4 ms: 1.11x slower                                              |
| bench_mp_pool            | 62.5 ms                                                     | 69.6 ms: 1.11x slower                                              |
| python_startup           | 18.7 ms                                                     | 21.1 ms: 1.13x slower                                              |
| unpickle_list            | 2.55 us                                                     | 2.89 us: 1.14x slower                                              |
| python_startup_no_site   | 15.9 ms                                                     | 18.1 ms: 1.14x slower                                              |
| async_generators         | 178 ms                                                      | 244 ms: 1.37x slower                                               |
| dask                     | 264 ms                                                      | 364 ms: 1.38x slower                                               |
| regex_v8                 | 13.8 ms                                                     | 26.0 ms: 1.88x slower                                              |
| Geometric mean           | (ref)                                                       | 1.04x faster                                                       |

Benchmark hidden because not significant (4): pickle_dict, pprint_pformat, coroutines, deepcopy_reduce
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
