
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: a47c13c
- commit date: 2023-08-19
- overall geometric mean: 1.03x faster
- HPT reliability: 56.88%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                     |
| tornado_http   | 91.8 ms                                                     | 88.2 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| nbody          | 70.0 ms                                                     | 79.6 ms: 1.14x slower                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 91.9 ms: 1.01x slower                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                       |
| regex_effbot   | 1.50 ms                                                     | 1.62 ms: 1.09x slower                                      |
| regex_v8       | 13.8 ms                                                     | 15.1 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.60 ms: 1.35x faster                                      |
| unpickle_pure_python | 152 us                                                      | 140 us: 1.08x faster                                       |
| xml_etree_parse      | 95.9 ms                                                     | 92.3 ms: 1.04x faster                                      |
| pickle_pure_python   | 200 us                                                      | 196 us: 1.02x faster                                       |
| xml_etree_process    | 37.1 ms                                                     | 38.3 ms: 1.03x slower                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.8 ms: 1.04x slower                                      |
| json_loads           | 12.9 us                                                     | 13.4 us: 1.04x slower                                      |
| tomli_loads          | 1.41 sec                                                    | 1.49 sec: 1.05x slower                                     |
| pickle_list          | 2.68 us                                                     | 2.85 us: 1.06x slower                                      |
| unpickle             | 8.09 us                                                     | 8.60 us: 1.06x slower                                      |
| xml_etree_generate   | 52.2 ms                                                     | 55.5 ms: 1.06x slower                                      |
| pickle               | 6.61 us                                                     | 7.37 us: 1.12x slower                                      |
| pickle_dict          | 18.5 us                                                     | 21.2 us: 1.15x slower                                      |
| unpickle_list        | 2.55 us                                                     | 2.99 us: 1.17x slower                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                      |
| python_startup         | 18.7 ms                                                     | 19.6 ms: 1.05x slower                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.41 ms: 1.02x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 97.8 us: 3.29x faster                                      |
| asyncio_tcp              | 699 ms                                                      | 475 ms: 1.47x faster                                       |
| generators               | 33.8 ms                                                     | 24.2 ms: 1.40x faster                                      |
| json_dumps               | 7.56 ms                                                     | 5.60 ms: 1.35x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 36.5 ns: 1.26x faster                                      |
| async_tree_none          | 320 ms                                                      | 266 ms: 1.20x faster                                       |
| raytrace                 | 211 ms                                                      | 176 ms: 1.20x faster                                       |
| coverage                 | 55.9 ms                                                     | 47.2 ms: 1.18x faster                                      |
| deltablue                | 2.61 ms                                                     | 2.22 ms: 1.18x faster                                      |
| mdp                      | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                     |
| sqlglot_parse            | 952 us                                                      | 829 us: 1.15x faster                                       |
| richards_super           | 37.5 ms                                                     | 32.7 ms: 1.15x faster                                      |
| chaos                    | 47.1 ms                                                     | 41.7 ms: 1.13x faster                                      |
| json                     | 3.25 ms                                                     | 2.89 ms: 1.13x faster                                      |
| sqlglot_transpile        | 1.16 ms                                                     | 1.05 ms: 1.11x faster                                      |
| logging_silent           | 69.8 ns                                                     | 63.7 ns: 1.10x faster                                      |
| comprehensions           | 15.9 us                                                     | 14.6 us: 1.09x faster                                      |
| unpickle_pure_python     | 152 us                                                      | 140 us: 1.08x faster                                       |
| async_tree_memoization   | 371 ms                                                      | 344 ms: 1.08x faster                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.97 sec: 1.07x faster                                     |
| crypto_pyaes             | 47.6 ms                                                     | 44.5 ms: 1.07x faster                                      |
| hexiom                   | 4.55 ms                                                     | 4.27 ms: 1.07x faster                                      |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 471 ms: 1.06x faster                                       |
| async_tree_io            | 779 ms                                                      | 733 ms: 1.06x faster                                       |
| go                       | 97.3 ms                                                     | 91.7 ms: 1.06x faster                                      |
| richards                 | 30.6 ms                                                     | 29.1 ms: 1.05x faster                                      |
| spectral_norm            | 67.9 ms                                                     | 64.7 ms: 1.05x faster                                      |
| nqueens                  | 64.9 ms                                                     | 62.2 ms: 1.04x faster                                      |
| tornado_http             | 91.8 ms                                                     | 88.2 ms: 1.04x faster                                      |
| xml_etree_parse          | 95.9 ms                                                     | 92.3 ms: 1.04x faster                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.49 ms: 1.03x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 61.6 ms: 1.03x faster                                      |
| bench_thread_pool        | 852 us                                                      | 828 us: 1.03x faster                                       |
| logging_format           | 7.01 us                                                     | 6.82 us: 1.03x faster                                      |
| logging_simple           | 6.61 us                                                     | 6.43 us: 1.03x faster                                      |
| deepcopy                 | 246 us                                                      | 240 us: 1.02x faster                                       |
| pickle_pure_python       | 200 us                                                      | 196 us: 1.02x faster                                       |
| deepcopy_memo            | 25.2 us                                                     | 24.8 us: 1.02x faster                                      |
| meteor_contest           | 74.7 ms                                                     | 73.9 ms: 1.01x faster                                      |
| sqlglot_normalize        | 190 ms                                                      | 188 ms: 1.01x faster                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 45.0 ms: 1.01x slower                                      |
| gc_traversal             | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 35.2 ms: 1.01x slower                                      |
| docutils                 | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                     |
| dulwich_log              | 44.5 ms                                                     | 45.1 ms: 1.01x slower                                      |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| regex_compile            | 90.6 ms                                                     | 91.9 ms: 1.01x slower                                      |
| mako                     | 7.26 ms                                                     | 7.41 ms: 1.02x slower                                      |
| xml_etree_process        | 37.1 ms                                                     | 38.3 ms: 1.03x slower                                      |
| pycparser                | 691 ms                                                      | 714 ms: 1.03x slower                                       |
| python_startup_no_site   | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                      |
| pprint_safe_repr         | 512 ms                                                      | 529 ms: 1.03x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.8 ms: 1.04x slower                                      |
| coroutines               | 14.6 ms                                                     | 15.2 ms: 1.04x slower                                      |
| sqlite_synth             | 1.68 us                                                     | 1.75 us: 1.04x slower                                      |
| pprint_pformat           | 1.04 sec                                                    | 1.08 sec: 1.04x slower                                     |
| json_loads               | 12.9 us                                                     | 13.4 us: 1.04x slower                                      |
| regex_dna                | 115 ms                                                      | 120 ms: 1.04x slower                                       |
| python_startup           | 18.7 ms                                                     | 19.6 ms: 1.05x slower                                      |
| create_gc_cycles         | 693 us                                                      | 727 us: 1.05x slower                                       |
| tomli_loads              | 1.41 sec                                                    | 1.49 sec: 1.05x slower                                     |
| bench_mp_pool            | 62.5 ms                                                     | 65.8 ms: 1.05x slower                                      |
| deepcopy_reduce          | 2.07 us                                                     | 2.19 us: 1.06x slower                                      |
| pickle_list              | 2.68 us                                                     | 2.85 us: 1.06x slower                                      |
| unpickle                 | 8.09 us                                                     | 8.60 us: 1.06x slower                                      |
| xml_etree_generate       | 52.2 ms                                                     | 55.5 ms: 1.06x slower                                      |
| scimark_fft              | 178 ms                                                      | 192 ms: 1.08x slower                                       |
| regex_effbot             | 1.50 ms                                                     | 1.62 ms: 1.09x slower                                      |
| regex_v8                 | 13.8 ms                                                     | 15.1 ms: 1.09x slower                                      |
| pathlib                  | 71.4 ms                                                     | 78.5 ms: 1.10x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 84.0 ms: 1.11x slower                                      |
| pickle                   | 6.61 us                                                     | 7.37 us: 1.12x slower                                      |
| nbody                    | 70.0 ms                                                     | 79.6 ms: 1.14x slower                                      |
| pickle_dict              | 18.5 us                                                     | 21.2 us: 1.15x slower                                      |
| unpickle_list            | 2.55 us                                                     | 2.99 us: 1.17x slower                                      |
| telco                    | 3.90 ms                                                     | 4.77 ms: 1.22x slower                                      |
| mypy2                    | 229 ms                                                      | 295 ms: 1.29x slower                                       |
| async_generators         | 178 ms                                                      | 244 ms: 1.37x slower                                       |
| dask                     | 264 ms                                                      | 372 ms: 1.41x slower                                       |
| Geometric mean           | (ref)                                                       | 1.03x faster                                               |

Benchmark hidden because not significant (3): float, pyflate, fannkuch
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 56.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
