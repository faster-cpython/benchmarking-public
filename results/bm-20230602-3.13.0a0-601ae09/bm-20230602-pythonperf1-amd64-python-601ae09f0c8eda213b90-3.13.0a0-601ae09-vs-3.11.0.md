
# Results vs. 3.11.0

- fork: python
- ref: 601ae09f0c8eda213b90
- machine: windows-amd64
- commit hash: 601ae09
- commit date: 2023-06-02
- overall geometric mean: 1.06x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tornado_http   | 91.8 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 54.0 ms: 1.01x faster                                                      |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 70.0 ms                                                     | 71.9 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 12.9 ms: 1.07x faster                                                      |
| regex_compile  | 90.6 ms                                                     | 86.7 ms: 1.05x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.68 ms: 1.33x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 132 us: 1.15x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 90.8 ms: 1.06x faster                                                      |
| pickle_pure_python   | 200 us                                                      | 191 us: 1.05x faster                                                       |
| tomli_loads          | 1.41 sec                                                    | 1.35 sec: 1.05x faster                                                     |
| pickle_dict          | 18.5 us                                                     | 18.0 us: 1.03x faster                                                      |
| xml_etree_process    | 37.1 ms                                                     | 37.8 ms: 1.02x slower                                                      |
| json_loads           | 12.9 us                                                     | 13.4 us: 1.04x slower                                                      |
| unpickle             | 8.09 us                                                     | 8.46 us: 1.05x slower                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 54.8 ms: 1.05x slower                                                      |
| pickle               | 6.61 us                                                     | 6.93 us: 1.05x slower                                                      |
| pickle_list          | 2.68 us                                                     | 2.83 us: 1.06x slower                                                      |
| unpickle_list        | 2.55 us                                                     | 2.86 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                      |
| python_startup_no_site | 15.9 ms                                                     | 15.5 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.79 ms: 1.07x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 91.2 us: 3.53x faster                                                      |
| generators               | 33.8 ms                                                     | 21.6 ms: 1.56x faster                                                      |
| asyncio_tcp              | 699 ms                                                      | 479 ms: 1.46x faster                                                       |
| json_dumps               | 7.56 ms                                                     | 5.68 ms: 1.33x faster                                                      |
| richards_super           | 37.5 ms                                                     | 29.2 ms: 1.28x faster                                                      |
| deltablue                | 2.61 ms                                                     | 2.07 ms: 1.26x faster                                                      |
| richards                 | 30.6 ms                                                     | 25.4 ms: 1.20x faster                                                      |
| sqlglot_parse            | 952 us                                                      | 791 us: 1.20x faster                                                       |
| logging_silent           | 69.8 ns                                                     | 59.4 ns: 1.18x faster                                                      |
| mdp                      | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                     |
| unpack_sequence          | 46.1 ns                                                     | 39.6 ns: 1.16x faster                                                      |
| sqlglot_transpile        | 1.16 ms                                                     | 1.00 ms: 1.16x faster                                                      |
| unpickle_pure_python     | 152 us                                                      | 132 us: 1.15x faster                                                       |
| comprehensions           | 15.9 us                                                     | 13.9 us: 1.14x faster                                                      |
| scimark_lu               | 63.5 ms                                                     | 55.8 ms: 1.14x faster                                                      |
| hexiom                   | 4.55 ms                                                     | 4.01 ms: 1.14x faster                                                      |
| raytrace                 | 211 ms                                                      | 187 ms: 1.13x faster                                                       |
| chaos                    | 47.1 ms                                                     | 42.1 ms: 1.12x faster                                                      |
| go                       | 97.3 ms                                                     | 87.6 ms: 1.11x faster                                                      |
| async_tree_none          | 320 ms                                                      | 292 ms: 1.10x faster                                                       |
| async_tree_memoization   | 371 ms                                                      | 340 ms: 1.09x faster                                                       |
| mypy2                    | 229 ms                                                      | 210 ms: 1.09x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.94 sec: 1.09x faster                                                     |
| regex_v8                 | 13.8 ms                                                     | 12.9 ms: 1.07x faster                                                      |
| mako                     | 7.26 ms                                                     | 6.79 ms: 1.07x faster                                                      |
| coverage                 | 55.9 ms                                                     | 52.3 ms: 1.07x faster                                                      |
| scimark_monte_carlo      | 44.6 ms                                                     | 41.8 ms: 1.07x faster                                                      |
| async_tree_io            | 779 ms                                                      | 731 ms: 1.06x faster                                                       |
| nqueens                  | 64.9 ms                                                     | 61.0 ms: 1.06x faster                                                      |
| xml_etree_parse          | 95.9 ms                                                     | 90.8 ms: 1.06x faster                                                      |
| deepcopy_memo            | 25.2 us                                                     | 23.9 us: 1.05x faster                                                      |
| tornado_http             | 91.8 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| pickle_pure_python       | 200 us                                                      | 191 us: 1.05x faster                                                       |
| tomli_loads              | 1.41 sec                                                    | 1.35 sec: 1.05x faster                                                     |
| deepcopy                 | 246 us                                                      | 235 us: 1.05x faster                                                       |
| spectral_norm            | 67.9 ms                                                     | 65.0 ms: 1.05x faster                                                      |
| regex_compile            | 90.6 ms                                                     | 86.7 ms: 1.05x faster                                                      |
| dulwich_log              | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                      |
| logging_simple           | 6.61 us                                                     | 6.34 us: 1.04x faster                                                      |
| scimark_fft              | 178 ms                                                      | 171 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 481 ms: 1.04x faster                                                       |
| pyflate                  | 304 ms                                                      | 292 ms: 1.04x faster                                                       |
| sqlglot_normalize        | 190 ms                                                      | 183 ms: 1.04x faster                                                       |
| coroutines               | 14.6 ms                                                     | 14.1 ms: 1.04x faster                                                      |
| logging_format           | 7.01 us                                                     | 6.81 us: 1.03x faster                                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.50 ms: 1.03x faster                                                      |
| bench_thread_pool        | 852 us                                                      | 828 us: 1.03x faster                                                       |
| python_startup           | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                      |
| pycparser                | 691 ms                                                      | 674 ms: 1.03x faster                                                       |
| python_startup_no_site   | 15.9 ms                                                     | 15.5 ms: 1.03x faster                                                      |
| pickle_dict              | 18.5 us                                                     | 18.0 us: 1.03x faster                                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 34.1 ms: 1.02x faster                                                      |
| crypto_pyaes             | 47.6 ms                                                     | 46.5 ms: 1.02x faster                                                      |
| float                    | 54.6 ms                                                     | 54.0 ms: 1.01x faster                                                      |
| meteor_contest           | 74.7 ms                                                     | 74.5 ms: 1.00x faster                                                      |
| pprint_pformat           | 1.04 sec                                                    | 1.04 sec: 1.00x slower                                                     |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| regex_dna                | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| gc_traversal             | 1.46 ms                                                     | 1.48 ms: 1.02x slower                                                      |
| xml_etree_process        | 37.1 ms                                                     | 37.8 ms: 1.02x slower                                                      |
| sqlite_synth             | 1.68 us                                                     | 1.72 us: 1.02x slower                                                      |
| nbody                    | 70.0 ms                                                     | 71.9 ms: 1.03x slower                                                      |
| telco                    | 3.90 ms                                                     | 4.03 ms: 1.03x slower                                                      |
| scimark_sor              | 75.6 ms                                                     | 78.1 ms: 1.03x slower                                                      |
| json_loads               | 12.9 us                                                     | 13.4 us: 1.04x slower                                                      |
| unpickle                 | 8.09 us                                                     | 8.46 us: 1.05x slower                                                      |
| create_gc_cycles         | 693 us                                                      | 725 us: 1.05x slower                                                       |
| regex_effbot             | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                      |
| xml_etree_generate       | 52.2 ms                                                     | 54.8 ms: 1.05x slower                                                      |
| pickle                   | 6.61 us                                                     | 6.93 us: 1.05x slower                                                      |
| bench_mp_pool            | 62.5 ms                                                     | 65.8 ms: 1.05x slower                                                      |
| pickle_list              | 2.68 us                                                     | 2.83 us: 1.06x slower                                                      |
| pathlib                  | 71.4 ms                                                     | 78.8 ms: 1.10x slower                                                      |
| unpickle_list            | 2.55 us                                                     | 2.86 us: 1.12x slower                                                      |
| async_generators         | 178 ms                                                      | 242 ms: 1.36x slower                                                       |
| dask                     | 264 ms                                                      | 361 ms: 1.36x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (6): json, pprint_safe_repr, xml_etree_iterparse, fannkuch, deepcopy_reduce, docutils
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
