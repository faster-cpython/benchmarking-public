
# Results vs. 3.11.0

- fork: python
- ref: be1b968dc1e63c3c68e1
- machine: windows-amd64
- commit hash: be1b968
- commit date: 2023-07-12
- overall geometric mean: 1.00x faster
- HPT reliability: 86.39%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                                     |
| tornado_http   | 91.8 ms                                                     | 89.8 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 54.6 ms                                                     | 56.9 ms: 1.04x slower                                                      |
| nbody          | 70.0 ms                                                     | 80.4 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 93.7 ms: 1.03x slower                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                                      |
| regex_v8       | 13.8 ms                                                     | 16.2 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.68 ms: 1.33x faster                                                      |
| xml_etree_parse      | 95.9 ms                                                     | 90.6 ms: 1.06x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 146 us: 1.04x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 18.8 us: 1.02x slower                                                      |
| pickle_pure_python   | 200 us                                                      | 204 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.1 ms: 1.04x slower                                                      |
| json_loads           | 12.9 us                                                     | 13.5 us: 1.05x slower                                                      |
| pickle_list          | 2.68 us                                                     | 2.82 us: 1.05x slower                                                      |
| xml_etree_process    | 37.1 ms                                                     | 39.3 ms: 1.06x slower                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 56.9 ms: 1.09x slower                                                      |
| pickle               | 6.61 us                                                     | 7.27 us: 1.10x slower                                                      |
| unpickle_list        | 2.55 us                                                     | 2.82 us: 1.11x slower                                                      |
| tomli_loads          | 1.41 sec                                                    | 1.59 sec: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 18.3 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.68 ms: 1.06x slower                                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230712-pythonperf1-amd64-python-be1b968dc1e63c3c68e1-3.13.0a0-be1b968 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 98.7 us: 3.26x faster                                                      |
| asyncio_tcp              | 699 ms                                                      | 480 ms: 1.46x faster                                                       |
| json_dumps               | 7.56 ms                                                     | 5.68 ms: 1.33x faster                                                      |
| generators               | 33.8 ms                                                     | 25.5 ms: 1.33x faster                                                      |
| mdp                      | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                                     |
| raytrace                 | 211 ms                                                      | 184 ms: 1.14x faster                                                       |
| deltablue                | 2.61 ms                                                     | 2.28 ms: 1.14x faster                                                      |
| json                     | 3.25 ms                                                     | 2.85 ms: 1.14x faster                                                      |
| richards_super           | 37.5 ms                                                     | 34.2 ms: 1.10x faster                                                      |
| sqlglot_parse            | 952 us                                                      | 870 us: 1.09x faster                                                       |
| unpack_sequence          | 46.1 ns                                                     | 42.6 ns: 1.08x faster                                                      |
| async_tree_none          | 320 ms                                                      | 300 ms: 1.07x faster                                                       |
| logging_silent           | 69.8 ns                                                     | 65.7 ns: 1.06x faster                                                      |
| chaos                    | 47.1 ms                                                     | 44.3 ms: 1.06x faster                                                      |
| coverage                 | 55.9 ms                                                     | 52.7 ms: 1.06x faster                                                      |
| xml_etree_parse          | 95.9 ms                                                     | 90.6 ms: 1.06x faster                                                      |
| sqlglot_transpile        | 1.16 ms                                                     | 1.10 ms: 1.06x faster                                                      |
| async_tree_memoization   | 371 ms                                                      | 351 ms: 1.06x faster                                                       |
| async_tree_io            | 779 ms                                                      | 739 ms: 1.05x faster                                                       |
| unpickle_pure_python     | 152 us                                                      | 146 us: 1.04x faster                                                       |
| mypy2                    | 229 ms                                                      | 221 ms: 1.04x faster                                                       |
| nqueens                  | 64.9 ms                                                     | 63.3 ms: 1.03x faster                                                      |
| python_startup           | 18.7 ms                                                     | 18.3 ms: 1.02x faster                                                      |
| tornado_http             | 91.8 ms                                                     | 89.8 ms: 1.02x faster                                                      |
| comprehensions           | 15.9 us                                                     | 15.6 us: 1.02x faster                                                      |
| bench_thread_pool        | 852 us                                                      | 835 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 492 ms: 1.02x faster                                                       |
| hexiom                   | 4.55 ms                                                     | 4.49 ms: 1.01x faster                                                      |
| scimark_lu               | 63.5 ms                                                     | 62.9 ms: 1.01x faster                                                      |
| crypto_pyaes             | 47.6 ms                                                     | 47.1 ms: 1.01x faster                                                      |
| richards                 | 30.6 ms                                                     | 30.4 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.59 ms: 1.01x slower                                                      |
| sqlglot_normalize        | 190 ms                                                      | 192 ms: 1.01x slower                                                       |
| gc_traversal             | 1.46 ms                                                     | 1.48 ms: 1.01x slower                                                      |
| meteor_contest           | 74.7 ms                                                     | 75.8 ms: 1.01x slower                                                      |
| scimark_monte_carlo      | 44.6 ms                                                     | 45.3 ms: 1.01x slower                                                      |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| pickle_dict              | 18.5 us                                                     | 18.8 us: 1.02x slower                                                      |
| deepcopy                 | 246 us                                                      | 250 us: 1.02x slower                                                       |
| pickle_pure_python       | 200 us                                                      | 204 us: 1.02x slower                                                       |
| go                       | 97.3 ms                                                     | 99.6 ms: 1.02x slower                                                      |
| spectral_norm            | 67.9 ms                                                     | 69.9 ms: 1.03x slower                                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 36.0 ms: 1.03x slower                                                      |
| regex_compile            | 90.6 ms                                                     | 93.7 ms: 1.03x slower                                                      |
| logging_simple           | 6.61 us                                                     | 6.88 us: 1.04x slower                                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.1 ms: 1.04x slower                                                      |
| float                    | 54.6 ms                                                     | 56.9 ms: 1.04x slower                                                      |
| regex_dna                | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| docutils                 | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                                     |
| json_loads               | 12.9 us                                                     | 13.5 us: 1.05x slower                                                      |
| bench_mp_pool            | 62.5 ms                                                     | 65.4 ms: 1.05x slower                                                      |
| create_gc_cycles         | 693 us                                                      | 728 us: 1.05x slower                                                       |
| pickle_list              | 2.68 us                                                     | 2.82 us: 1.05x slower                                                      |
| coroutines               | 14.6 ms                                                     | 15.4 ms: 1.05x slower                                                      |
| logging_format           | 7.01 us                                                     | 7.38 us: 1.05x slower                                                      |
| deepcopy_memo            | 25.2 us                                                     | 26.5 us: 1.05x slower                                                      |
| sqlite_synth             | 1.68 us                                                     | 1.77 us: 1.05x slower                                                      |
| mako                     | 7.26 ms                                                     | 7.68 ms: 1.06x slower                                                      |
| pyflate                  | 304 ms                                                      | 322 ms: 1.06x slower                                                       |
| xml_etree_process        | 37.1 ms                                                     | 39.3 ms: 1.06x slower                                                      |
| fannkuch                 | 252 ms                                                      | 267 ms: 1.06x slower                                                       |
| regex_effbot             | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                                      |
| pprint_safe_repr         | 512 ms                                                      | 545 ms: 1.06x slower                                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.11 sec: 1.07x slower                                                     |
| deepcopy_reduce          | 2.07 us                                                     | 2.22 us: 1.07x slower                                                      |
| scimark_fft              | 178 ms                                                      | 191 ms: 1.07x slower                                                       |
| xml_etree_generate       | 52.2 ms                                                     | 56.9 ms: 1.09x slower                                                      |
| pickle                   | 6.61 us                                                     | 7.27 us: 1.10x slower                                                      |
| pathlib                  | 71.4 ms                                                     | 78.7 ms: 1.10x slower                                                      |
| unpickle_list            | 2.55 us                                                     | 2.82 us: 1.11x slower                                                      |
| telco                    | 3.90 ms                                                     | 4.34 ms: 1.11x slower                                                      |
| tomli_loads              | 1.41 sec                                                    | 1.59 sec: 1.12x slower                                                     |
| pycparser                | 691 ms                                                      | 787 ms: 1.14x slower                                                       |
| nbody                    | 70.0 ms                                                     | 80.4 ms: 1.15x slower                                                      |
| regex_v8                 | 13.8 ms                                                     | 16.2 ms: 1.17x slower                                                      |
| scimark_sor              | 75.6 ms                                                     | 89.3 ms: 1.18x slower                                                      |
| async_generators         | 178 ms                                                      | 244 ms: 1.38x slower                                                       |
| dask                     | 264 ms                                                      | 387 ms: 1.46x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (4): python_startup_no_site, asyncio_tcp_ssl, dulwich_log, unpickle
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 86.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
