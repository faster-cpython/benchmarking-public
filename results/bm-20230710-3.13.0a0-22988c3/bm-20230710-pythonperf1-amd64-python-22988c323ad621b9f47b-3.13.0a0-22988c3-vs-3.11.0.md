
# Results vs. 3.11.0

- fork: python
- ref: 22988c323ad621b9f47b
- machine: windows-amd64
- commit hash: 22988c3
- commit date: 2023-07-10
- overall geometric mean: 1.01x faster
- HPT reliability: 89.94%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                                     |
| tornado_http   | 91.8 ms                                                     | 98.7 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 54.6 ms                                                     | 55.7 ms: 1.02x slower                                                      |
| nbody          | 70.0 ms                                                     | 75.9 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 93.5 ms: 1.03x slower                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.77 ms: 1.31x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 141 us: 1.07x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 91.2 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.4 ms: 1.03x slower                                                      |
| unpickle             | 8.09 us                                                     | 8.45 us: 1.04x slower                                                      |
| xml_etree_process    | 37.1 ms                                                     | 38.8 ms: 1.05x slower                                                      |
| pickle_list          | 2.68 us                                                     | 2.82 us: 1.05x slower                                                      |
| json_loads           | 12.9 us                                                     | 13.6 us: 1.06x slower                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 55.9 ms: 1.07x slower                                                      |
| pickle               | 6.61 us                                                     | 7.12 us: 1.08x slower                                                      |
| tomli_loads          | 1.41 sec                                                    | 1.59 sec: 1.12x slower                                                     |
| unpickle_list        | 2.55 us                                                     | 2.94 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (2): pickle_dict, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 19.9 ms: 1.06x slower                                                      |
| python_startup_no_site | 15.9 ms                                                     | 16.9 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.47 ms: 1.03x slower                                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 96.7 us: 3.33x faster                                                      |
| generators               | 33.8 ms                                                     | 24.6 ms: 1.37x faster                                                      |
| json_dumps               | 7.56 ms                                                     | 5.77 ms: 1.31x faster                                                      |
| asyncio_tcp              | 699 ms                                                      | 545 ms: 1.28x faster                                                       |
| mdp                      | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                     |
| raytrace                 | 211 ms                                                      | 182 ms: 1.16x faster                                                       |
| json                     | 3.25 ms                                                     | 2.83 ms: 1.15x faster                                                      |
| deltablue                | 2.61 ms                                                     | 2.31 ms: 1.13x faster                                                      |
| unpack_sequence          | 46.1 ns                                                     | 41.1 ns: 1.12x faster                                                      |
| richards_super           | 37.5 ms                                                     | 34.2 ms: 1.10x faster                                                      |
| chaos                    | 47.1 ms                                                     | 43.1 ms: 1.09x faster                                                      |
| sqlglot_parse            | 952 us                                                      | 875 us: 1.09x faster                                                       |
| logging_silent           | 69.8 ns                                                     | 64.4 ns: 1.08x faster                                                      |
| coverage                 | 55.9 ms                                                     | 51.5 ms: 1.08x faster                                                      |
| async_tree_none          | 320 ms                                                      | 297 ms: 1.08x faster                                                       |
| unpickle_pure_python     | 152 us                                                      | 141 us: 1.07x faster                                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.10 ms: 1.06x faster                                                      |
| async_tree_memoization   | 371 ms                                                      | 352 ms: 1.05x faster                                                       |
| xml_etree_parse          | 95.9 ms                                                     | 91.2 ms: 1.05x faster                                                      |
| crypto_pyaes             | 47.6 ms                                                     | 45.4 ms: 1.05x faster                                                      |
| async_tree_io            | 779 ms                                                      | 743 ms: 1.05x faster                                                       |
| comprehensions           | 15.9 us                                                     | 15.2 us: 1.05x faster                                                      |
| hexiom                   | 4.55 ms                                                     | 4.39 ms: 1.04x faster                                                      |
| nqueens                  | 64.9 ms                                                     | 62.8 ms: 1.03x faster                                                      |
| mypy2                    | 229 ms                                                      | 223 ms: 1.03x faster                                                       |
| scimark_lu               | 63.5 ms                                                     | 61.8 ms: 1.03x faster                                                      |
| spectral_norm            | 67.9 ms                                                     | 66.3 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 490 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.52 ms: 1.02x faster                                                      |
| scimark_monte_carlo      | 44.6 ms                                                     | 43.9 ms: 1.02x faster                                                      |
| richards                 | 30.6 ms                                                     | 30.1 ms: 1.02x faster                                                      |
| go                       | 97.3 ms                                                     | 98.4 ms: 1.01x slower                                                      |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| deepcopy                 | 246 us                                                      | 249 us: 1.01x slower                                                       |
| sqlglot_normalize        | 190 ms                                                      | 193 ms: 1.02x slower                                                       |
| fannkuch                 | 252 ms                                                      | 257 ms: 1.02x slower                                                       |
| deepcopy_memo            | 25.2 us                                                     | 25.7 us: 1.02x slower                                                      |
| float                    | 54.6 ms                                                     | 55.7 ms: 1.02x slower                                                      |
| logging_simple           | 6.61 us                                                     | 6.78 us: 1.02x slower                                                      |
| mako                     | 7.26 ms                                                     | 7.47 ms: 1.03x slower                                                      |
| gc_traversal             | 1.46 ms                                                     | 1.50 ms: 1.03x slower                                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.4 ms: 1.03x slower                                                      |
| dulwich_log              | 44.5 ms                                                     | 45.8 ms: 1.03x slower                                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 36.0 ms: 1.03x slower                                                      |
| regex_compile            | 90.6 ms                                                     | 93.5 ms: 1.03x slower                                                      |
| pyflate                  | 304 ms                                                      | 315 ms: 1.04x slower                                                       |
| pprint_safe_repr         | 512 ms                                                      | 532 ms: 1.04x slower                                                       |
| logging_format           | 7.01 us                                                     | 7.30 us: 1.04x slower                                                      |
| docutils                 | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                                     |
| sqlite_synth             | 1.68 us                                                     | 1.76 us: 1.04x slower                                                      |
| unpickle                 | 8.09 us                                                     | 8.45 us: 1.04x slower                                                      |
| xml_etree_process        | 37.1 ms                                                     | 38.8 ms: 1.05x slower                                                      |
| regex_dna                | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.09 sec: 1.05x slower                                                     |
| scimark_fft              | 178 ms                                                      | 187 ms: 1.05x slower                                                       |
| pickle_list              | 2.68 us                                                     | 2.82 us: 1.05x slower                                                      |
| deepcopy_reduce          | 2.07 us                                                     | 2.18 us: 1.05x slower                                                      |
| create_gc_cycles         | 693 us                                                      | 729 us: 1.05x slower                                                       |
| json_loads               | 12.9 us                                                     | 13.6 us: 1.06x slower                                                      |
| coroutines               | 14.6 ms                                                     | 15.5 ms: 1.06x slower                                                      |
| python_startup           | 18.7 ms                                                     | 19.9 ms: 1.06x slower                                                      |
| python_startup_no_site   | 15.9 ms                                                     | 16.9 ms: 1.07x slower                                                      |
| pycparser                | 691 ms                                                      | 738 ms: 1.07x slower                                                       |
| bench_mp_pool            | 62.5 ms                                                     | 66.9 ms: 1.07x slower                                                      |
| xml_etree_generate       | 52.2 ms                                                     | 55.9 ms: 1.07x slower                                                      |
| tornado_http             | 91.8 ms                                                     | 98.7 ms: 1.07x slower                                                      |
| pickle                   | 6.61 us                                                     | 7.12 us: 1.08x slower                                                      |
| regex_effbot             | 1.50 ms                                                     | 1.61 ms: 1.08x slower                                                      |
| nbody                    | 70.0 ms                                                     | 75.9 ms: 1.08x slower                                                      |
| scimark_sor              | 75.6 ms                                                     | 84.4 ms: 1.12x slower                                                      |
| tomli_loads              | 1.41 sec                                                    | 1.59 sec: 1.12x slower                                                     |
| unpickle_list            | 2.55 us                                                     | 2.94 us: 1.16x slower                                                      |
| pathlib                  | 71.4 ms                                                     | 83.1 ms: 1.17x slower                                                      |
| telco                    | 3.90 ms                                                     | 4.72 ms: 1.21x slower                                                      |
| async_generators         | 178 ms                                                      | 243 ms: 1.37x slower                                                       |
| dask                     | 264 ms                                                      | 388 ms: 1.47x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (6): pickle_dict, bench_thread_pool, meteor_contest, pickle_pure_python, regex_v8, asyncio_tcp_ssl
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 89.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
