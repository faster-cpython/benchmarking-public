
# Results vs. 3.10.4

- fork: python
- ref: 601ae09f0c8eda213b90
- machine: windows-amd64
- commit hash: 601ae09
- commit date: 2023-06-02
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.61 sec: 1.17x faster                                                     |
| tornado_http   | 109 ms                                                      | 87.5 ms: 1.25x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.0 ms: 1.12x faster                                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                                       |
| nbody          | 69.3 ms                                                     | 71.9 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 86.7 ms: 1.19x faster                                                      |
| regex_v8       | 15.0 ms                                                     | 12.9 ms: 1.16x faster                                                      |
| regex_dna      | 132 ms                                                      | 117 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.68 ms: 1.50x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 191 us: 1.34x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 132 us: 1.30x faster                                                       |
| tomli_loads          | 1.62 sec                                                    | 1.35 sec: 1.20x faster                                                     |
| xml_etree_process    | 43.4 ms                                                     | 37.8 ms: 1.15x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 90.8 ms: 1.12x faster                                                      |
| unpickle             | 9.17 us                                                     | 8.46 us: 1.08x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.4 us: 1.05x faster                                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.7 ms: 1.01x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 54.8 ms: 1.00x slower                                                      |
| unpickle_list        | 2.81 us                                                     | 2.86 us: 1.02x slower                                                      |
| pickle               | 6.80 us                                                     | 6.93 us: 1.02x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 18.0 us: 1.07x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.83 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.79 ms: 1.30x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 91.2 us: 3.56x faster                                                      |
| deltablue                | 4.17 ms                                                     | 2.07 ms: 2.01x faster                                                      |
| richards_super           | 51.7 ms                                                     | 29.2 ms: 1.77x faster                                                      |
| mypy2                    | 352 ms                                                      | 210 ms: 1.67x faster                                                       |
| richards                 | 41.2 ms                                                     | 25.4 ms: 1.62x faster                                                      |
| logging_silent           | 96.4 ns                                                     | 59.4 ns: 1.62x faster                                                      |
| go                       | 136 ms                                                      | 87.6 ms: 1.55x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 791 us: 1.54x faster                                                       |
| scimark_lu               | 85.4 ms                                                     | 55.8 ms: 1.53x faster                                                      |
| json_dumps               | 8.50 ms                                                     | 5.68 ms: 1.50x faster                                                      |
| asyncio_tcp              | 712 ms                                                      | 479 ms: 1.49x faster                                                       |
| async_tree_memoization   | 497 ms                                                      | 340 ms: 1.46x faster                                                       |
| generators               | 31.6 ms                                                     | 21.6 ms: 1.46x faster                                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.00 ms: 1.46x faster                                                      |
| async_tree_io            | 1.07 sec                                                    | 731 ms: 1.46x faster                                                       |
| raytrace                 | 271 ms                                                      | 187 ms: 1.45x faster                                                       |
| async_tree_none          | 420 ms                                                      | 292 ms: 1.44x faster                                                       |
| chaos                    | 58.9 ms                                                     | 42.1 ms: 1.40x faster                                                      |
| hexiom                   | 5.52 ms                                                     | 4.01 ms: 1.38x faster                                                      |
| pickle_pure_python       | 257 us                                                      | 191 us: 1.34x faster                                                       |
| scimark_sor              | 105 ms                                                      | 78.1 ms: 1.34x faster                                                      |
| crypto_pyaes             | 62.3 ms                                                     | 46.5 ms: 1.34x faster                                                      |
| scimark_monte_carlo      | 55.9 ms                                                     | 41.8 ms: 1.34x faster                                                      |
| pyflate                  | 387 ms                                                      | 292 ms: 1.32x faster                                                       |
| mako                     | 8.80 ms                                                     | 6.79 ms: 1.30x faster                                                      |
| unpickle_pure_python     | 171 us                                                      | 132 us: 1.30x faster                                                       |
| pycparser                | 868 ms                                                      | 674 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 481 ms: 1.27x faster                                                       |
| tornado_http             | 109 ms                                                      | 87.5 ms: 1.25x faster                                                      |
| spectral_norm            | 78.0 ms                                                     | 65.0 ms: 1.20x faster                                                      |
| tomli_loads              | 1.62 sec                                                    | 1.35 sec: 1.20x faster                                                     |
| mdp                      | 1.71 sec                                                    | 1.43 sec: 1.20x faster                                                     |
| regex_compile            | 103 ms                                                      | 86.7 ms: 1.19x faster                                                      |
| deepcopy_memo            | 28.5 us                                                     | 23.9 us: 1.19x faster                                                      |
| docutils                 | 1.89 sec                                                    | 1.61 sec: 1.17x faster                                                     |
| regex_v8                 | 15.0 ms                                                     | 12.9 ms: 1.16x faster                                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.04 sec: 1.16x faster                                                     |
| pprint_safe_repr         | 589 ms                                                      | 511 ms: 1.15x faster                                                       |
| xml_etree_process        | 43.4 ms                                                     | 37.8 ms: 1.15x faster                                                      |
| comprehensions           | 16.0 us                                                     | 13.9 us: 1.15x faster                                                      |
| bench_thread_pool        | 946 us                                                      | 828 us: 1.14x faster                                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 34.1 ms: 1.14x faster                                                      |
| scimark_fft              | 193 ms                                                      | 171 ms: 1.13x faster                                                       |
| coroutines               | 15.9 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| regex_dna                | 132 ms                                                      | 117 ms: 1.13x faster                                                       |
| xml_etree_parse          | 102 ms                                                      | 90.8 ms: 1.12x faster                                                      |
| dulwich_log              | 47.6 ms                                                     | 42.5 ms: 1.12x faster                                                      |
| float                    | 60.2 ms                                                     | 54.0 ms: 1.12x faster                                                      |
| sqlglot_normalize        | 202 ms                                                      | 183 ms: 1.10x faster                                                       |
| nqueens                  | 67.0 ms                                                     | 61.0 ms: 1.10x faster                                                      |
| python_startup           | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                      |
| deepcopy                 | 255 us                                                      | 235 us: 1.09x faster                                                       |
| unpickle                 | 9.17 us                                                     | 8.46 us: 1.08x faster                                                      |
| create_gc_cycles         | 782 us                                                      | 725 us: 1.08x faster                                                       |
| sqlite_synth             | 1.84 us                                                     | 1.72 us: 1.07x faster                                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.50 ms: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| json_loads               | 14.2 us                                                     | 13.4 us: 1.05x faster                                                      |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.94 sec: 1.05x faster                                                     |
| deepcopy_reduce          | 2.16 us                                                     | 2.08 us: 1.04x faster                                                      |
| fannkuch                 | 258 ms                                                      | 253 ms: 1.02x faster                                                       |
| xml_etree_iterparse      | 63.5 ms                                                     | 62.7 ms: 1.01x faster                                                      |
| xml_etree_generate       | 54.5 ms                                                     | 54.8 ms: 1.00x slower                                                      |
| unpickle_list            | 2.81 us                                                     | 2.86 us: 1.02x slower                                                      |
| pathlib                  | 77.4 ms                                                     | 78.8 ms: 1.02x slower                                                      |
| pickle                   | 6.80 us                                                     | 6.93 us: 1.02x slower                                                      |
| logging_simple           | 6.20 us                                                     | 6.34 us: 1.02x slower                                                      |
| logging_format           | 6.66 us                                                     | 6.81 us: 1.02x slower                                                      |
| meteor_contest           | 72.5 ms                                                     | 74.5 ms: 1.03x slower                                                      |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                                       |
| nbody                    | 69.3 ms                                                     | 71.9 ms: 1.04x slower                                                      |
| unpack_sequence          | 37.8 ns                                                     | 39.6 ns: 1.05x slower                                                      |
| telco                    | 3.78 ms                                                     | 4.03 ms: 1.07x slower                                                      |
| pickle_dict              | 16.9 us                                                     | 18.0 us: 1.07x slower                                                      |
| async_generators         | 224 ms                                                      | 242 ms: 1.08x slower                                                       |
| bench_mp_pool            | 60.7 ms                                                     | 65.8 ms: 1.08x slower                                                      |
| pickle_list              | 2.59 us                                                     | 2.83 us: 1.09x slower                                                      |
| gc_traversal             | 1.34 ms                                                     | 1.48 ms: 1.10x slower                                                      |
| dask                     | 305 ms                                                      | 361 ms: 1.18x slower                                                       |
| coverage                 | 40.0 ms                                                     | 52.3 ms: 1.31x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (2): python_startup_no_site, json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
