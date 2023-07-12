
# Results vs. 3.11.0

- fork: faster-cpython
- ref: split_load_global
- machine: windows-amd64
- commit hash: 1bbc515
- commit date: 2023-07-12
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.64 sec: 1.03x slower                                                            |
| tornado_http   | 91.8 ms                                                     | 90.1 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                              |
| float          | 54.6 ms                                                     | 56.1 ms: 1.03x slower                                                             |
| nbody          | 70.0 ms                                                     | 81.2 ms: 1.16x slower                                                             |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                             |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                              |
| regex_compile  | 90.6 ms                                                     | 93.0 ms: 1.03x slower                                                             |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.70 ms: 1.33x faster                                                             |
| xml_etree_parse      | 95.9 ms                                                     | 93.0 ms: 1.03x faster                                                             |
| unpickle_pure_python | 152 us                                                      | 148 us: 1.03x faster                                                              |
| unpickle             | 8.09 us                                                     | 8.18 us: 1.01x slower                                                             |
| pickle_pure_python   | 200 us                                                      | 204 us: 1.02x slower                                                              |
| json_loads           | 12.9 us                                                     | 13.5 us: 1.05x slower                                                             |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.9 ms: 1.05x slower                                                             |
| pickle_list          | 2.68 us                                                     | 2.83 us: 1.06x slower                                                             |
| xml_etree_process    | 37.1 ms                                                     | 39.7 ms: 1.07x slower                                                             |
| pickle               | 6.61 us                                                     | 7.11 us: 1.08x slower                                                             |
| unpickle_list        | 2.55 us                                                     | 2.76 us: 1.09x slower                                                             |
| xml_etree_generate   | 52.2 ms                                                     | 57.0 ms: 1.09x slower                                                             |
| tomli_loads          | 1.41 sec                                                    | 1.61 sec: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 18.4 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.51 ms: 1.03x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.1 us: 3.38x faster                                                             |
| asyncio_tcp              | 699 ms                                                      | 482 ms: 1.45x faster                                                              |
| generators               | 33.8 ms                                                     | 24.2 ms: 1.40x faster                                                             |
| json_dumps               | 7.56 ms                                                     | 5.70 ms: 1.33x faster                                                             |
| mdp                      | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                            |
| raytrace                 | 211 ms                                                      | 187 ms: 1.13x faster                                                              |
| deltablue                | 2.61 ms                                                     | 2.33 ms: 1.12x faster                                                             |
| json                     | 3.25 ms                                                     | 2.91 ms: 1.12x faster                                                             |
| richards_super           | 37.5 ms                                                     | 34.2 ms: 1.10x faster                                                             |
| sqlglot_parse            | 952 us                                                      | 876 us: 1.09x faster                                                              |
| async_tree_none          | 320 ms                                                      | 298 ms: 1.08x faster                                                              |
| chaos                    | 47.1 ms                                                     | 44.1 ms: 1.07x faster                                                             |
| logging_silent           | 69.8 ns                                                     | 65.4 ns: 1.07x faster                                                             |
| coverage                 | 55.9 ms                                                     | 52.5 ms: 1.06x faster                                                             |
| sqlglot_transpile        | 1.16 ms                                                     | 1.10 ms: 1.06x faster                                                             |
| async_tree_memoization   | 371 ms                                                      | 351 ms: 1.06x faster                                                              |
| async_tree_io            | 779 ms                                                      | 745 ms: 1.04x faster                                                              |
| mypy2                    | 229 ms                                                      | 220 ms: 1.04x faster                                                              |
| crypto_pyaes             | 47.6 ms                                                     | 46.0 ms: 1.03x faster                                                             |
| xml_etree_parse          | 95.9 ms                                                     | 93.0 ms: 1.03x faster                                                             |
| unpickle_pure_python     | 152 us                                                      | 148 us: 1.03x faster                                                              |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 491 ms: 1.02x faster                                                              |
| tornado_http             | 91.8 ms                                                     | 90.1 ms: 1.02x faster                                                             |
| comprehensions           | 15.9 us                                                     | 15.6 us: 1.02x faster                                                             |
| python_startup           | 18.7 ms                                                     | 18.4 ms: 1.02x faster                                                             |
| nqueens                  | 64.9 ms                                                     | 63.7 ms: 1.02x faster                                                             |
| regex_v8                 | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                             |
| richards                 | 30.6 ms                                                     | 30.4 ms: 1.01x faster                                                             |
| meteor_contest           | 74.7 ms                                                     | 75.1 ms: 1.01x slower                                                             |
| hexiom                   | 4.55 ms                                                     | 4.58 ms: 1.01x slower                                                             |
| deepcopy                 | 246 us                                                      | 248 us: 1.01x slower                                                              |
| unpickle                 | 8.09 us                                                     | 8.18 us: 1.01x slower                                                             |
| scimark_monte_carlo      | 44.6 ms                                                     | 45.2 ms: 1.01x slower                                                             |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                                              |
| sqlglot_normalize        | 190 ms                                                      | 193 ms: 1.02x slower                                                              |
| regex_dna                | 115 ms                                                      | 117 ms: 1.02x slower                                                              |
| gc_traversal             | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                                             |
| pickle_pure_python       | 200 us                                                      | 204 us: 1.02x slower                                                              |
| regex_compile            | 90.6 ms                                                     | 93.0 ms: 1.03x slower                                                             |
| float                    | 54.6 ms                                                     | 56.1 ms: 1.03x slower                                                             |
| docutils                 | 1.60 sec                                                    | 1.64 sec: 1.03x slower                                                            |
| mako                     | 7.26 ms                                                     | 7.51 ms: 1.03x slower                                                             |
| sqlglot_optimize         | 34.9 ms                                                     | 36.1 ms: 1.03x slower                                                             |
| go                       | 97.3 ms                                                     | 101 ms: 1.04x slower                                                              |
| coroutines               | 14.6 ms                                                     | 15.2 ms: 1.04x slower                                                             |
| spectral_norm            | 67.9 ms                                                     | 70.6 ms: 1.04x slower                                                             |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.68 ms: 1.04x slower                                                             |
| bench_mp_pool            | 62.5 ms                                                     | 65.3 ms: 1.04x slower                                                             |
| json_loads               | 12.9 us                                                     | 13.5 us: 1.05x slower                                                             |
| create_gc_cycles         | 693 us                                                      | 726 us: 1.05x slower                                                              |
| sqlite_synth             | 1.68 us                                                     | 1.77 us: 1.05x slower                                                             |
| deepcopy_memo            | 25.2 us                                                     | 26.4 us: 1.05x slower                                                             |
| regex_effbot             | 1.50 ms                                                     | 1.58 ms: 1.05x slower                                                             |
| deepcopy_reduce          | 2.07 us                                                     | 2.18 us: 1.05x slower                                                             |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.9 ms: 1.05x slower                                                             |
| fannkuch                 | 252 ms                                                      | 266 ms: 1.05x slower                                                              |
| pickle_list              | 2.68 us                                                     | 2.83 us: 1.06x slower                                                             |
| logging_simple           | 6.61 us                                                     | 7.00 us: 1.06x slower                                                             |
| pyflate                  | 304 ms                                                      | 322 ms: 1.06x slower                                                              |
| pprint_safe_repr         | 512 ms                                                      | 542 ms: 1.06x slower                                                              |
| pprint_pformat           | 1.04 sec                                                    | 1.11 sec: 1.07x slower                                                            |
| scimark_fft              | 178 ms                                                      | 190 ms: 1.07x slower                                                              |
| xml_etree_process        | 37.1 ms                                                     | 39.7 ms: 1.07x slower                                                             |
| logging_format           | 7.01 us                                                     | 7.53 us: 1.07x slower                                                             |
| pickle                   | 6.61 us                                                     | 7.11 us: 1.08x slower                                                             |
| unpickle_list            | 2.55 us                                                     | 2.76 us: 1.09x slower                                                             |
| xml_etree_generate       | 52.2 ms                                                     | 57.0 ms: 1.09x slower                                                             |
| pycparser                | 691 ms                                                      | 758 ms: 1.10x slower                                                              |
| pathlib                  | 71.4 ms                                                     | 78.5 ms: 1.10x slower                                                             |
| tomli_loads              | 1.41 sec                                                    | 1.61 sec: 1.14x slower                                                            |
| telco                    | 3.90 ms                                                     | 4.46 ms: 1.14x slower                                                             |
| nbody                    | 70.0 ms                                                     | 81.2 ms: 1.16x slower                                                             |
| scimark_sor              | 75.6 ms                                                     | 88.9 ms: 1.18x slower                                                             |
| async_generators         | 178 ms                                                      | 242 ms: 1.37x slower                                                              |
| dask                     | 264 ms                                                      | 385 ms: 1.46x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.01x faster                                                                      |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, pickle_dict, bench_thread_pool, python_startup_no_site, unpack_sequence, scimark_lu, dulwich_log
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
