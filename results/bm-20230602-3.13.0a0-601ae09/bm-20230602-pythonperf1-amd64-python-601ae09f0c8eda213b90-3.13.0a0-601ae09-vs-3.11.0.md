
# Results vs. 3.11.0

- fork: python
- ref: 601ae09f0c8eda213b90
- machine: windows-amd64
- commit hash: 601ae09
- commit date: 2023-06-02
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tornado_http   | 91.8 ms                                                     | 87.1 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 67.2 ms: 1.04x faster                                                      |
| float          | 54.6 ms                                                     | 53.4 ms: 1.02x faster                                                      |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 85.9 ms: 1.06x faster                                                      |
| regex_v8       | 13.8 ms                                                     | 13.2 ms: 1.05x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.53 ms: 1.37x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 128 us: 1.19x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 189 us: 1.06x faster                                                       |
| tomli_loads          | 1.41 sec                                                    | 1.34 sec: 1.06x faster                                                     |
| xml_etree_parse      | 95.9 ms                                                     | 92.4 ms: 1.04x faster                                                      |
| xml_etree_process    | 37.1 ms                                                     | 37.4 ms: 1.01x slower                                                      |
| unpickle             | 8.09 us                                                     | 8.19 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                                      |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 55.4 ms: 1.06x slower                                                      |
| pickle_list          | 2.68 us                                                     | 2.87 us: 1.07x slower                                                      |
| unpickle_list        | 2.55 us                                                     | 2.79 us: 1.10x slower                                                      |
| pickle               | 6.61 us                                                     | 7.33 us: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.69 ms: 1.09x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 91.5 us: 3.52x faster                                                      |
| generators               | 33.8 ms                                                     | 21.4 ms: 1.58x faster                                                      |
| asyncio_tcp              | 699 ms                                                      | 469 ms: 1.49x faster                                                       |
| json_dumps               | 7.56 ms                                                     | 5.53 ms: 1.37x faster                                                      |
| richards_super           | 37.5 ms                                                     | 29.7 ms: 1.26x faster                                                      |
| unpack_sequence          | 46.1 ns                                                     | 36.6 ns: 1.26x faster                                                      |
| deltablue                | 2.61 ms                                                     | 2.12 ms: 1.23x faster                                                      |
| sqlglot_parse            | 952 us                                                      | 786 us: 1.21x faster                                                       |
| unpickle_pure_python     | 152 us                                                      | 128 us: 1.19x faster                                                       |
| richards                 | 30.6 ms                                                     | 25.8 ms: 1.18x faster                                                      |
| mdp                      | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                     |
| logging_silent           | 69.8 ns                                                     | 59.8 ns: 1.17x faster                                                      |
| sqlglot_transpile        | 1.16 ms                                                     | 1.00 ms: 1.16x faster                                                      |
| hexiom                   | 4.55 ms                                                     | 4.00 ms: 1.14x faster                                                      |
| comprehensions           | 15.9 us                                                     | 14.0 us: 1.14x faster                                                      |
| scimark_lu               | 63.5 ms                                                     | 55.8 ms: 1.14x faster                                                      |
| chaos                    | 47.1 ms                                                     | 41.8 ms: 1.13x faster                                                      |
| go                       | 97.3 ms                                                     | 87.0 ms: 1.12x faster                                                      |
| raytrace                 | 211 ms                                                      | 188 ms: 1.12x faster                                                       |
| async_tree_none          | 320 ms                                                      | 287 ms: 1.11x faster                                                       |
| async_tree_memoization   | 371 ms                                                      | 340 ms: 1.09x faster                                                       |
| json                     | 3.25 ms                                                     | 2.98 ms: 1.09x faster                                                      |
| mypy2                    | 229 ms                                                      | 211 ms: 1.09x faster                                                       |
| mako                     | 7.26 ms                                                     | 6.69 ms: 1.09x faster                                                      |
| deepcopy_memo            | 25.2 us                                                     | 23.5 us: 1.07x faster                                                      |
| spectral_norm            | 67.9 ms                                                     | 63.4 ms: 1.07x faster                                                      |
| nqueens                  | 64.9 ms                                                     | 60.6 ms: 1.07x faster                                                      |
| coverage                 | 55.9 ms                                                     | 52.3 ms: 1.07x faster                                                      |
| async_tree_io            | 779 ms                                                      | 732 ms: 1.06x faster                                                       |
| logging_simple           | 6.61 us                                                     | 6.24 us: 1.06x faster                                                      |
| deepcopy                 | 246 us                                                      | 233 us: 1.06x faster                                                       |
| pickle_pure_python       | 200 us                                                      | 189 us: 1.06x faster                                                       |
| regex_compile            | 90.6 ms                                                     | 85.9 ms: 1.06x faster                                                      |
| tomli_loads              | 1.41 sec                                                    | 1.34 sec: 1.06x faster                                                     |
| tornado_http             | 91.8 ms                                                     | 87.1 ms: 1.05x faster                                                      |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.3 ms: 1.05x faster                                                      |
| bench_thread_pool        | 852 us                                                      | 809 us: 1.05x faster                                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.45 ms: 1.05x faster                                                      |
| regex_v8                 | 13.8 ms                                                     | 13.2 ms: 1.05x faster                                                      |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 478 ms: 1.05x faster                                                       |
| coroutines               | 14.6 ms                                                     | 14.0 ms: 1.05x faster                                                      |
| sqlglot_normalize        | 190 ms                                                      | 182 ms: 1.05x faster                                                       |
| pyflate                  | 304 ms                                                      | 291 ms: 1.04x faster                                                       |
| logging_format           | 7.01 us                                                     | 6.73 us: 1.04x faster                                                      |
| nbody                    | 70.0 ms                                                     | 67.2 ms: 1.04x faster                                                      |
| fannkuch                 | 252 ms                                                      | 242 ms: 1.04x faster                                                       |
| xml_etree_parse          | 95.9 ms                                                     | 92.4 ms: 1.04x faster                                                      |
| dulwich_log              | 44.5 ms                                                     | 42.9 ms: 1.04x faster                                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 33.7 ms: 1.03x faster                                                      |
| crypto_pyaes             | 47.6 ms                                                     | 46.0 ms: 1.03x faster                                                      |
| pprint_safe_repr         | 512 ms                                                      | 497 ms: 1.03x faster                                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.01 sec: 1.03x faster                                                     |
| meteor_contest           | 74.7 ms                                                     | 72.8 ms: 1.03x faster                                                      |
| pycparser                | 691 ms                                                      | 674 ms: 1.03x faster                                                       |
| float                    | 54.6 ms                                                     | 53.4 ms: 1.02x faster                                                      |
| scimark_fft              | 178 ms                                                      | 175 ms: 1.02x faster                                                       |
| xml_etree_process        | 37.1 ms                                                     | 37.4 ms: 1.01x slower                                                      |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| unpickle                 | 8.09 us                                                     | 8.19 us: 1.01x slower                                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                                      |
| regex_dna                | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| gc_traversal             | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                                      |
| scimark_sor              | 75.6 ms                                                     | 77.5 ms: 1.03x slower                                                      |
| sqlite_synth             | 1.68 us                                                     | 1.73 us: 1.03x slower                                                      |
| create_gc_cycles         | 693 us                                                      | 718 us: 1.04x slower                                                       |
| telco                    | 3.90 ms                                                     | 4.05 ms: 1.04x slower                                                      |
| regex_effbot             | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                      |
| bench_mp_pool            | 62.5 ms                                                     | 65.8 ms: 1.05x slower                                                      |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                                      |
| xml_etree_generate       | 52.2 ms                                                     | 55.4 ms: 1.06x slower                                                      |
| pickle_list              | 2.68 us                                                     | 2.87 us: 1.07x slower                                                      |
| unpickle_list            | 2.55 us                                                     | 2.79 us: 1.10x slower                                                      |
| pathlib                  | 71.4 ms                                                     | 79.0 ms: 1.11x slower                                                      |
| pickle                   | 6.61 us                                                     | 7.33 us: 1.11x slower                                                      |
| async_generators         | 178 ms                                                      | 242 ms: 1.36x slower                                                       |
| dask                     | 264 ms                                                      | 360 ms: 1.36x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (6): asyncio_tcp_ssl, python_startup, deepcopy_reduce, python_startup_no_site, pickle_dict, docutils
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
