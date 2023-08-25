
# Results vs. 3.10.4

- fork: python
- ref: 601ae09f0c8eda213b90
- machine: windows-amd64
- commit hash: 601ae09
- commit date: 2023-06-02
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.61 sec: 1.17x faster                                                     |
| tornado_http   | 109 ms                                                      | 87.1 ms: 1.25x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.4 ms: 1.13x faster                                                      |
| nbody          | 69.3 ms                                                     | 67.2 ms: 1.03x faster                                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.9 ms: 1.20x faster                                                      |
| regex_v8       | 15.0 ms                                                     | 13.2 ms: 1.14x faster                                                      |
| regex_dna      | 132 ms                                                      | 117 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.53 ms: 1.54x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 189 us: 1.35x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 128 us: 1.34x faster                                                       |
| tomli_loads          | 1.62 sec                                                    | 1.34 sec: 1.21x faster                                                     |
| xml_etree_process    | 43.4 ms                                                     | 37.4 ms: 1.16x faster                                                      |
| unpickle             | 9.17 us                                                     | 8.19 us: 1.12x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 92.4 ms: 1.10x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.04x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 55.4 ms: 1.02x slower                                                      |
| pickle               | 6.80 us                                                     | 7.33 us: 1.08x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 18.6 us: 1.10x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.87 us: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.6 ms: 1.07x faster                                                      |
| python_startup_no_site | 15.5 ms                                                     | 15.9 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.69 ms: 1.32x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 91.5 us: 3.55x faster                                                      |
| deltablue                | 4.17 ms                                                     | 2.12 ms: 1.96x faster                                                      |
| richards_super           | 51.7 ms                                                     | 29.7 ms: 1.74x faster                                                      |
| mypy2                    | 352 ms                                                      | 211 ms: 1.67x faster                                                       |
| logging_silent           | 96.4 ns                                                     | 59.8 ns: 1.61x faster                                                      |
| richards                 | 41.2 ms                                                     | 25.8 ms: 1.60x faster                                                      |
| go                       | 136 ms                                                      | 87.0 ms: 1.57x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 786 us: 1.55x faster                                                       |
| json_dumps               | 8.50 ms                                                     | 5.53 ms: 1.54x faster                                                      |
| scimark_lu               | 85.4 ms                                                     | 55.8 ms: 1.53x faster                                                      |
| asyncio_tcp              | 712 ms                                                      | 469 ms: 1.52x faster                                                       |
| generators               | 31.6 ms                                                     | 21.4 ms: 1.47x faster                                                      |
| async_tree_memoization   | 497 ms                                                      | 340 ms: 1.46x faster                                                       |
| async_tree_none          | 420 ms                                                      | 287 ms: 1.46x faster                                                       |
| sqlglot_transpile        | 1.46 ms                                                     | 1.00 ms: 1.46x faster                                                      |
| async_tree_io            | 1.07 sec                                                    | 732 ms: 1.45x faster                                                       |
| raytrace                 | 271 ms                                                      | 188 ms: 1.44x faster                                                       |
| chaos                    | 58.9 ms                                                     | 41.8 ms: 1.41x faster                                                      |
| hexiom                   | 5.52 ms                                                     | 4.00 ms: 1.38x faster                                                      |
| pickle_pure_python       | 257 us                                                      | 189 us: 1.35x faster                                                       |
| crypto_pyaes             | 62.3 ms                                                     | 46.0 ms: 1.35x faster                                                      |
| scimark_sor              | 105 ms                                                      | 77.5 ms: 1.35x faster                                                      |
| unpickle_pure_python     | 171 us                                                      | 128 us: 1.34x faster                                                       |
| pyflate                  | 387 ms                                                      | 291 ms: 1.33x faster                                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.3 ms: 1.32x faster                                                      |
| mako                     | 8.80 ms                                                     | 6.69 ms: 1.32x faster                                                      |
| pycparser                | 868 ms                                                      | 674 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 478 ms: 1.27x faster                                                       |
| tornado_http             | 109 ms                                                      | 87.1 ms: 1.25x faster                                                      |
| spectral_norm            | 78.0 ms                                                     | 63.4 ms: 1.23x faster                                                      |
| deepcopy_memo            | 28.5 us                                                     | 23.5 us: 1.21x faster                                                      |
| tomli_loads              | 1.62 sec                                                    | 1.34 sec: 1.21x faster                                                     |
| mdp                      | 1.71 sec                                                    | 1.42 sec: 1.21x faster                                                     |
| regex_compile            | 103 ms                                                      | 85.9 ms: 1.20x faster                                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.01 sec: 1.19x faster                                                     |
| pprint_safe_repr         | 589 ms                                                      | 497 ms: 1.18x faster                                                       |
| docutils                 | 1.89 sec                                                    | 1.61 sec: 1.17x faster                                                     |
| bench_thread_pool        | 946 us                                                      | 809 us: 1.17x faster                                                       |
| xml_etree_process        | 43.4 ms                                                     | 37.4 ms: 1.16x faster                                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 33.7 ms: 1.15x faster                                                      |
| comprehensions           | 16.0 us                                                     | 14.0 us: 1.14x faster                                                      |
| coroutines               | 15.9 ms                                                     | 14.0 ms: 1.14x faster                                                      |
| regex_v8                 | 15.0 ms                                                     | 13.2 ms: 1.14x faster                                                      |
| regex_dna                | 132 ms                                                      | 117 ms: 1.13x faster                                                       |
| float                    | 60.2 ms                                                     | 53.4 ms: 1.13x faster                                                      |
| unpickle                 | 9.17 us                                                     | 8.19 us: 1.12x faster                                                      |
| sqlglot_normalize        | 202 ms                                                      | 182 ms: 1.11x faster                                                       |
| dulwich_log              | 47.6 ms                                                     | 42.9 ms: 1.11x faster                                                      |
| scimark_fft              | 193 ms                                                      | 175 ms: 1.11x faster                                                       |
| nqueens                  | 67.0 ms                                                     | 60.6 ms: 1.11x faster                                                      |
| xml_etree_parse          | 102 ms                                                      | 92.4 ms: 1.10x faster                                                      |
| deepcopy                 | 255 us                                                      | 233 us: 1.10x faster                                                       |
| create_gc_cycles         | 782 us                                                      | 718 us: 1.09x faster                                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.45 ms: 1.09x faster                                                      |
| python_startup           | 20.0 ms                                                     | 18.6 ms: 1.07x faster                                                      |
| sqlite_synth             | 1.84 us                                                     | 1.73 us: 1.06x faster                                                      |
| fannkuch                 | 258 ms                                                      | 242 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.07 us: 1.04x faster                                                      |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.04x faster                                                      |
| unpack_sequence          | 37.8 ns                                                     | 36.6 ns: 1.03x faster                                                      |
| nbody                    | 69.3 ms                                                     | 67.2 ms: 1.03x faster                                                      |
| meteor_contest           | 72.5 ms                                                     | 72.8 ms: 1.00x slower                                                      |
| logging_simple           | 6.20 us                                                     | 6.24 us: 1.01x slower                                                      |
| logging_format           | 6.66 us                                                     | 6.73 us: 1.01x slower                                                      |
| xml_etree_generate       | 54.5 ms                                                     | 55.4 ms: 1.02x slower                                                      |
| pathlib                  | 77.4 ms                                                     | 79.0 ms: 1.02x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 15.9 ms: 1.03x slower                                                      |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                                       |
| telco                    | 3.78 ms                                                     | 4.05 ms: 1.07x slower                                                      |
| pickle                   | 6.80 us                                                     | 7.33 us: 1.08x slower                                                      |
| async_generators         | 224 ms                                                      | 242 ms: 1.08x slower                                                       |
| bench_mp_pool            | 60.7 ms                                                     | 65.8 ms: 1.08x slower                                                      |
| pickle_dict              | 16.9 us                                                     | 18.6 us: 1.10x slower                                                      |
| gc_traversal             | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                                      |
| pickle_list              | 2.59 us                                                     | 2.87 us: 1.11x slower                                                      |
| dask                     | 305 ms                                                      | 360 ms: 1.18x slower                                                       |
| coverage                 | 40.0 ms                                                     | 52.3 ms: 1.31x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (4): json, asyncio_tcp_ssl, unpickle_list, xml_etree_iterparse
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.11x
