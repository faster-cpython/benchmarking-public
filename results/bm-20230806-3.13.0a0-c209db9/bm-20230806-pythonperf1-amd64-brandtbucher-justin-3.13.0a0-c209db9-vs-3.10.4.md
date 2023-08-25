
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.08x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.76 sec: 1.07x faster                                             |
| tornado_http   | 109 ms                                                      | 91.5 ms: 1.19x faster                                              |
| Geometric mean | (ref)                                                       | 1.13x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 57.6 ms: 1.05x faster                                              |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                               |
| nbody          | 69.3 ms                                                     | 79.8 ms: 1.15x slower                                              |
| Geometric mean | (ref)                                                       | 1.05x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                              |
| regex_dna      | 132 ms                                                      | 124 ms: 1.07x faster                                               |
| regex_compile  | 103 ms                                                      | 98.0 ms: 1.05x faster                                              |
| regex_effbot   | 1.66 ms                                                     | 1.68 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                       | 1.04x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.86 ms: 1.45x faster                                              |
| pickle_pure_python   | 257 us                                                      | 204 us: 1.26x faster                                               |
| unpickle_pure_python | 171 us                                                      | 154 us: 1.11x faster                                               |
| xml_etree_parse      | 102 ms                                                      | 92.7 ms: 1.10x faster                                              |
| xml_etree_process    | 43.4 ms                                                     | 40.4 ms: 1.08x faster                                              |
| unpickle             | 9.17 us                                                     | 8.61 us: 1.07x faster                                              |
| json_loads           | 14.2 us                                                     | 13.9 us: 1.02x faster                                              |
| tomli_loads          | 1.62 sec                                                    | 1.64 sec: 1.01x slower                                             |
| pickle               | 6.80 us                                                     | 7.05 us: 1.04x slower                                              |
| xml_etree_iterparse  | 63.5 ms                                                     | 68.0 ms: 1.07x slower                                              |
| xml_etree_generate   | 54.5 ms                                                     | 58.8 ms: 1.08x slower                                              |
| unpickle_list        | 2.81 us                                                     | 3.04 us: 1.08x slower                                              |
| pickle_dict          | 16.9 us                                                     | 18.6 us: 1.10x slower                                              |
| pickle_list          | 2.59 us                                                     | 2.88 us: 1.11x slower                                              |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.4 ms: 1.03x faster                                              |
| python_startup_no_site | 15.5 ms                                                     | 16.7 ms: 1.08x slower                                              |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.39 ms: 1.19x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 98.0 us: 3.31x faster                                              |
| deltablue                | 4.17 ms                                                     | 2.42 ms: 1.72x faster                                              |
| mypy2                    | 352 ms                                                      | 232 ms: 1.52x faster                                               |
| richards_super           | 51.7 ms                                                     | 35.0 ms: 1.48x faster                                              |
| json_dumps               | 8.50 ms                                                     | 5.86 ms: 1.45x faster                                              |
| logging_silent           | 96.4 ns                                                     | 67.8 ns: 1.42x faster                                              |
| asyncio_tcp              | 712 ms                                                      | 508 ms: 1.40x faster                                               |
| raytrace                 | 271 ms                                                      | 195 ms: 1.39x faster                                               |
| async_tree_io            | 1.07 sec                                                    | 771 ms: 1.38x faster                                               |
| async_tree_memoization   | 497 ms                                                      | 368 ms: 1.35x faster                                               |
| sqlglot_parse            | 1.22 ms                                                     | 912 us: 1.34x faster                                               |
| async_tree_none          | 420 ms                                                      | 319 ms: 1.32x faster                                               |
| scimark_lu               | 85.4 ms                                                     | 65.4 ms: 1.31x faster                                              |
| richards                 | 41.2 ms                                                     | 31.6 ms: 1.30x faster                                              |
| crypto_pyaes             | 62.3 ms                                                     | 48.4 ms: 1.29x faster                                              |
| go                       | 136 ms                                                      | 107 ms: 1.27x faster                                               |
| sqlglot_transpile        | 1.46 ms                                                     | 1.15 ms: 1.27x faster                                              |
| pickle_pure_python       | 257 us                                                      | 204 us: 1.26x faster                                               |
| chaos                    | 58.9 ms                                                     | 47.9 ms: 1.23x faster                                              |
| scimark_monte_carlo      | 55.9 ms                                                     | 46.2 ms: 1.21x faster                                              |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 510 ms: 1.19x faster                                               |
| tornado_http             | 109 ms                                                      | 91.5 ms: 1.19x faster                                              |
| mako                     | 8.80 ms                                                     | 7.39 ms: 1.19x faster                                              |
| generators               | 31.6 ms                                                     | 27.0 ms: 1.17x faster                                              |
| pyflate                  | 387 ms                                                      | 334 ms: 1.16x faster                                               |
| scimark_sor              | 105 ms                                                      | 91.9 ms: 1.14x faster                                              |
| pycparser                | 868 ms                                                      | 778 ms: 1.12x faster                                               |
| unpickle_pure_python     | 171 us                                                      | 154 us: 1.11x faster                                               |
| xml_etree_parse          | 102 ms                                                      | 92.7 ms: 1.10x faster                                              |
| bench_thread_pool        | 946 us                                                      | 864 us: 1.10x faster                                               |
| mdp                      | 1.71 sec                                                    | 1.57 sec: 1.09x faster                                             |
| hexiom                   | 5.52 ms                                                     | 5.06 ms: 1.09x faster                                              |
| xml_etree_process        | 43.4 ms                                                     | 40.4 ms: 1.08x faster                                              |
| docutils                 | 1.89 sec                                                    | 1.76 sec: 1.07x faster                                             |
| regex_v8                 | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                              |
| regex_dna                | 132 ms                                                      | 124 ms: 1.07x faster                                               |
| unpickle                 | 9.17 us                                                     | 8.61 us: 1.07x faster                                              |
| deepcopy_memo            | 28.5 us                                                     | 26.8 us: 1.06x faster                                              |
| pprint_pformat           | 1.21 sec                                                    | 1.14 sec: 1.06x faster                                             |
| regex_compile            | 103 ms                                                      | 98.0 ms: 1.05x faster                                              |
| pprint_safe_repr         | 589 ms                                                      | 561 ms: 1.05x faster                                               |
| sqlglot_optimize         | 39.0 ms                                                     | 37.2 ms: 1.05x faster                                              |
| float                    | 60.2 ms                                                     | 57.6 ms: 1.05x faster                                              |
| spectral_norm            | 78.0 ms                                                     | 74.9 ms: 1.04x faster                                              |
| create_gc_cycles         | 782 us                                                      | 751 us: 1.04x faster                                               |
| python_startup           | 20.0 ms                                                     | 19.4 ms: 1.03x faster                                              |
| coroutines               | 15.9 ms                                                     | 15.5 ms: 1.03x faster                                              |
| json_loads               | 14.2 us                                                     | 13.9 us: 1.02x faster                                              |
| sqlite_synth             | 1.84 us                                                     | 1.81 us: 1.01x faster                                              |
| dulwich_log              | 47.6 ms                                                     | 48.1 ms: 1.01x slower                                              |
| tomli_loads              | 1.62 sec                                                    | 1.64 sec: 1.01x slower                                             |
| regex_effbot             | 1.66 ms                                                     | 1.68 ms: 1.01x slower                                              |
| deepcopy                 | 255 us                                                      | 261 us: 1.02x slower                                               |
| pickle                   | 6.80 us                                                     | 7.05 us: 1.04x slower                                              |
| comprehensions           | 16.0 us                                                     | 16.6 us: 1.04x slower                                              |
| scimark_fft              | 193 ms                                                      | 201 ms: 1.04x slower                                               |
| pidigits                 | 145 ms                                                      | 151 ms: 1.04x slower                                               |
| deepcopy_reduce          | 2.16 us                                                     | 2.31 us: 1.07x slower                                              |
| xml_etree_iterparse      | 63.5 ms                                                     | 68.0 ms: 1.07x slower                                              |
| python_startup_no_site   | 15.5 ms                                                     | 16.7 ms: 1.08x slower                                              |
| xml_etree_generate       | 54.5 ms                                                     | 58.8 ms: 1.08x slower                                              |
| unpickle_list            | 2.81 us                                                     | 3.04 us: 1.08x slower                                              |
| pathlib                  | 77.4 ms                                                     | 84.4 ms: 1.09x slower                                              |
| pickle_dict              | 16.9 us                                                     | 18.6 us: 1.10x slower                                              |
| fannkuch                 | 258 ms                                                      | 284 ms: 1.10x slower                                               |
| unpack_sequence          | 37.8 ns                                                     | 42.0 ns: 1.11x slower                                              |
| pickle_list              | 2.59 us                                                     | 2.88 us: 1.11x slower                                              |
| async_generators         | 224 ms                                                      | 252 ms: 1.13x slower                                               |
| logging_simple           | 6.20 us                                                     | 7.01 us: 1.13x slower                                              |
| meteor_contest           | 72.5 ms                                                     | 82.1 ms: 1.13x slower                                              |
| logging_format           | 6.66 us                                                     | 7.54 us: 1.13x slower                                              |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 3.01 ms: 1.13x slower                                              |
| gc_traversal             | 1.34 ms                                                     | 1.53 ms: 1.14x slower                                              |
| nbody                    | 69.3 ms                                                     | 79.8 ms: 1.15x slower                                              |
| bench_mp_pool            | 60.7 ms                                                     | 71.1 ms: 1.17x slower                                              |
| telco                    | 3.78 ms                                                     | 4.88 ms: 1.29x slower                                              |
| dask                     | 305 ms                                                      | 398 ms: 1.31x slower                                               |
| coverage                 | 40.0 ms                                                     | 52.7 ms: 1.32x slower                                              |
| Geometric mean           | (ref)                                                       | 1.08x faster                                                       |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, json, sqlglot_normalize, nqueens
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
