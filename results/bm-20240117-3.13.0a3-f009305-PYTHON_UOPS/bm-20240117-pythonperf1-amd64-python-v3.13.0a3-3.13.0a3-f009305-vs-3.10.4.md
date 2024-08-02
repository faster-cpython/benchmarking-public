
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                            |
| chameleon      | 5.79 ms                                                     | 5.10 ms: 1.13x faster                                           |
| docutils       | 1.92 sec                                                    | 1.59 sec: 1.21x faster                                          |
| tornado_http   | 108 ms                                                      | 88.2 ms: 1.23x faster                                           |
| Geometric mean | (ref)                                                       | 1.17x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 266 ms: 1.64x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 341 ms: 1.54x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 722 ms: 1.53x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 450 ms: 1.42x faster                                            |
| Geometric mean          | (ref)                                                       | 1.53x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.5 ms: 1.11x faster                                           |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| nbody          | 71.3 ms                                                     | 79.2 ms: 1.11x slower                                           |
| Geometric mean | (ref)                                                       | 1.00x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 84.2 ms: 1.26x faster                                           |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                           |
| regex_v8       | 15.4 ms                                                     | 15.5 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                       | 1.10x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                           |
| pickle_pure_python   | 270 us                                                      | 182 us: 1.48x faster                                            |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.34x faster                                            |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                          |
| xml_etree_process    | 44.5 ms                                                     | 37.3 ms: 1.19x faster                                           |
| unpickle             | 9.09 us                                                     | 8.21 us: 1.11x faster                                           |
| json_loads           | 14.0 us                                                     | 13.6 us: 1.03x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 94.0 ms: 1.03x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 55.2 ms: 1.01x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 67.5 ms: 1.04x slower                                           |
| pickle               | 6.85 us                                                     | 7.37 us: 1.08x slower                                           |
| pickle_dict          | 17.2 us                                                     | 18.8 us: 1.09x slower                                           |
| pickle_list          | 2.75 us                                                     | 3.08 us: 1.12x slower                                           |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.5 ms: 1.19x slower                                           |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 9.03 ms                                                     | 7.29 ms: 1.24x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 74.9 us: 4.48x faster                                           |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                           |
| logging_silent           | 94.6 ns                                                     | 55.3 ns: 1.71x faster                                           |
| json_dumps               | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                           |
| async_tree_none          | 435 ms                                                      | 266 ms: 1.64x faster                                            |
| deltablue                | 4.19 ms                                                     | 2.60 ms: 1.61x faster                                           |
| generators               | 32.4 ms                                                     | 20.6 ms: 1.57x faster                                           |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                           |
| raytrace                 | 273 ms                                                      | 174 ms: 1.57x faster                                            |
| asyncio_tcp              | 732 ms                                                      | 468 ms: 1.56x faster                                            |
| sqlglot_parse            | 1.22 ms                                                     | 778 us: 1.56x faster                                            |
| async_tree_memoization   | 526 ms                                                      | 341 ms: 1.54x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 722 ms: 1.53x faster                                            |
| go                       | 139 ms                                                      | 90.8 ms: 1.53x faster                                           |
| scimark_lu               | 85.8 ms                                                     | 56.9 ms: 1.51x faster                                           |
| pickle_pure_python       | 270 us                                                      | 182 us: 1.48x faster                                            |
| sqlglot_transpile        | 1.48 ms                                                     | 1000 us: 1.48x faster                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 450 ms: 1.42x faster                                            |
| chaos                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                           |
| pycparser                | 930 ms                                                      | 675 ms: 1.38x faster                                            |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.34x faster                                            |
| scimark_sor              | 106 ms                                                      | 79.9 ms: 1.33x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 47.7 ms: 1.31x faster                                           |
| mypy2                    | 555 ms                                                      | 424 ms: 1.31x faster                                            |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.62 sec: 1.30x faster                                          |
| comprehensions           | 16.5 us                                                     | 12.7 us: 1.30x faster                                           |
| pyflate                  | 409 ms                                                      | 323 ms: 1.27x faster                                            |
| regex_compile            | 106 ms                                                      | 84.2 ms: 1.26x faster                                           |
| mako                     | 9.03 ms                                                     | 7.29 ms: 1.24x faster                                           |
| coroutines               | 16.0 ms                                                     | 12.9 ms: 1.24x faster                                           |
| sympy_sum                | 107 ms                                                      | 86.6 ms: 1.24x faster                                           |
| tornado_http             | 108 ms                                                      | 88.2 ms: 1.23x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                           |
| dask                     | 313 ms                                                      | 257 ms: 1.22x faster                                            |
| deepcopy_memo            | 28.8 us                                                     | 23.7 us: 1.21x faster                                           |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                          |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                          |
| docutils                 | 1.92 sec                                                    | 1.59 sec: 1.21x faster                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.5 ms: 1.21x faster                                           |
| xml_etree_process        | 44.5 ms                                                     | 37.3 ms: 1.19x faster                                           |
| hexiom                   | 5.74 ms                                                     | 4.82 ms: 1.19x faster                                           |
| dulwich_log              | 50.5 ms                                                     | 42.6 ms: 1.18x faster                                           |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                            |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.17x faster                                           |
| sqlglot_optimize         | 39.8 ms                                                     | 34.6 ms: 1.15x faster                                           |
| sqlglot_normalize        | 205 ms                                                      | 180 ms: 1.14x faster                                            |
| chameleon                | 5.79 ms                                                     | 5.10 ms: 1.13x faster                                           |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                            |
| sympy_expand             | 314 ms                                                      | 279 ms: 1.13x faster                                            |
| pprint_safe_repr         | 592 ms                                                      | 528 ms: 1.12x faster                                            |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                            |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                          |
| float                    | 61.7 ms                                                     | 55.5 ms: 1.11x faster                                           |
| deepcopy                 | 255 us                                                      | 230 us: 1.11x faster                                            |
| unpickle                 | 9.09 us                                                     | 8.21 us: 1.11x faster                                           |
| bench_thread_pool        | 958 us                                                      | 867 us: 1.10x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                           |
| create_gc_cycles         | 800 us                                                      | 738 us: 1.08x faster                                            |
| nqueens                  | 66.6 ms                                                     | 63.0 ms: 1.06x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                           |
| json_loads               | 14.0 us                                                     | 13.6 us: 1.03x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 94.0 ms: 1.03x faster                                           |
| unpack_sequence          | 39.6 ns                                                     | 39.1 ns: 1.01x faster                                           |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| logging_format           | 6.76 us                                                     | 6.70 us: 1.01x faster                                           |
| xml_etree_generate       | 55.5 ms                                                     | 55.2 ms: 1.01x faster                                           |
| meteor_contest           | 75.9 ms                                                     | 76.2 ms: 1.00x slower                                           |
| regex_v8                 | 15.4 ms                                                     | 15.5 ms: 1.01x slower                                           |
| async_generators         | 222 ms                                                      | 227 ms: 1.03x slower                                            |
| fannkuch                 | 256 ms                                                      | 264 ms: 1.03x slower                                            |
| spectral_norm            | 77.3 ms                                                     | 79.9 ms: 1.03x slower                                           |
| pathlib                  | 75.7 ms                                                     | 78.3 ms: 1.03x slower                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 67.5 ms: 1.04x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.49 ms: 1.06x slower                                           |
| pickle                   | 6.85 us                                                     | 7.37 us: 1.08x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 67.1 ms: 1.08x slower                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.95 ms: 1.08x slower                                           |
| scimark_fft              | 187 ms                                                      | 203 ms: 1.08x slower                                            |
| pickle_dict              | 17.2 us                                                     | 18.8 us: 1.09x slower                                           |
| nbody                    | 71.3 ms                                                     | 79.2 ms: 1.11x slower                                           |
| pickle_list              | 2.75 us                                                     | 3.08 us: 1.12x slower                                           |
| json                     | 3.14 ms                                                     | 3.52 ms: 1.12x slower                                           |
| coverage                 | 39.0 ms                                                     | 46.0 ms: 1.18x slower                                           |
| telco                    | 3.94 ms                                                     | 4.66 ms: 1.18x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 18.5 ms: 1.19x slower                                           |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                    |

Benchmark hidden because not significant (3): logging_simple, python_startup, unpickle_list
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x


# Memory

- memory change: unknown