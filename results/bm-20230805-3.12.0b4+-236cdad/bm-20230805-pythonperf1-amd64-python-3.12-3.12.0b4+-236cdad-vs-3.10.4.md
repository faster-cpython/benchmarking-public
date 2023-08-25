
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 236cdad
- commit date: 2023-08-05
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 214 ms: 1.11x faster                                        |
| docutils       | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                      |
| tornado_http   | 109 ms                                                      | 89.3 ms: 1.22x faster                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.7 ms: 1.10x faster                                       |
| nbody          | 69.3 ms                                                     | 70.1 ms: 1.01x slower                                       |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 86.9 ms: 1.19x faster                                       |
| regex_v8       | 15.0 ms                                                     | 14.0 ms: 1.07x faster                                       |
| regex_dna      | 132 ms                                                      | 124 ms: 1.06x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.64 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.76 ms: 1.48x faster                                       |
| pickle_pure_python   | 257 us                                                      | 197 us: 1.30x faster                                        |
| unpickle_pure_python | 171 us                                                      | 135 us: 1.27x faster                                        |
| tomli_loads          | 1.62 sec                                                    | 1.37 sec: 1.18x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 38.5 ms: 1.13x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 90.6 ms: 1.12x faster                                       |
| unpickle             | 9.17 us                                                     | 8.48 us: 1.08x faster                                       |
| json_loads           | 14.2 us                                                     | 13.6 us: 1.04x faster                                       |
| xml_etree_generate   | 54.5 ms                                                     | 56.6 ms: 1.04x slower                                       |
| pickle               | 6.80 us                                                     | 7.24 us: 1.06x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.5 us: 1.09x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.88 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.9 ms: 1.03x slower                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.20 ms: 1.22x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf1-amd64-python-3.12-3.12.0b4+-236cdad |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 100.0 us: 3.25x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.20 ms: 1.90x faster                                       |
| richards_super           | 51.7 ms                                                     | 29.4 ms: 1.76x faster                                       |
| mypy2                    | 352 ms                                                      | 213 ms: 1.65x faster                                        |
| logging_silent           | 96.4 ns                                                     | 60.8 ns: 1.59x faster                                       |
| richards                 | 41.2 ms                                                     | 26.1 ms: 1.58x faster                                       |
| go                       | 136 ms                                                      | 86.9 ms: 1.57x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 823 us: 1.48x faster                                        |
| json_dumps               | 8.50 ms                                                     | 5.76 ms: 1.48x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 58.5 ms: 1.46x faster                                       |
| asyncio_tcp              | 712 ms                                                      | 491 ms: 1.45x faster                                        |
| async_tree_io            | 1.07 sec                                                    | 744 ms: 1.43x faster                                        |
| async_tree_memoization   | 497 ms                                                      | 348 ms: 1.43x faster                                        |
| raytrace                 | 271 ms                                                      | 191 ms: 1.42x faster                                        |
| async_tree_none          | 420 ms                                                      | 298 ms: 1.41x faster                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 1.04 ms: 1.41x faster                                       |
| generators               | 31.6 ms                                                     | 22.7 ms: 1.39x faster                                       |
| chaos                    | 58.9 ms                                                     | 42.9 ms: 1.37x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.12 ms: 1.34x faster                                       |
| scimark_sor              | 105 ms                                                      | 78.4 ms: 1.34x faster                                       |
| pickle_pure_python       | 257 us                                                      | 197 us: 1.30x faster                                        |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.2 ms: 1.29x faster                                       |
| pyflate                  | 387 ms                                                      | 301 ms: 1.28x faster                                        |
| crypto_pyaes             | 62.3 ms                                                     | 48.9 ms: 1.27x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 135 us: 1.27x faster                                        |
| pycparser                | 868 ms                                                      | 692 ms: 1.25x faster                                        |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 488 ms: 1.25x faster                                        |
| mako                     | 8.80 ms                                                     | 7.20 ms: 1.22x faster                                       |
| tornado_http             | 109 ms                                                      | 89.3 ms: 1.22x faster                                       |
| spectral_norm            | 78.0 ms                                                     | 64.2 ms: 1.21x faster                                       |
| deepcopy_memo            | 28.5 us                                                     | 23.7 us: 1.20x faster                                       |
| regex_compile            | 103 ms                                                      | 86.9 ms: 1.19x faster                                       |
| tomli_loads              | 1.62 sec                                                    | 1.37 sec: 1.18x faster                                      |
| mdp                      | 1.71 sec                                                    | 1.46 sec: 1.17x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.04 sec: 1.16x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 514 ms: 1.15x faster                                        |
| docutils                 | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                      |
| aiohttp                  | 1.01 ms                                                     | 886 us: 1.14x faster                                        |
| xml_etree_process        | 43.4 ms                                                     | 38.5 ms: 1.13x faster                                       |
| comprehensions           | 16.0 us                                                     | 14.2 us: 1.13x faster                                       |
| xml_etree_parse          | 102 ms                                                      | 90.6 ms: 1.12x faster                                       |
| coroutines               | 15.9 ms                                                     | 14.2 ms: 1.12x faster                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 35.0 ms: 1.11x faster                                       |
| 2to3                     | 237 ms                                                      | 214 ms: 1.11x faster                                        |
| bench_thread_pool        | 946 us                                                      | 858 us: 1.10x faster                                        |
| float                    | 60.2 ms                                                     | 54.7 ms: 1.10x faster                                       |
| fannkuch                 | 258 ms                                                      | 234 ms: 1.10x faster                                        |
| deepcopy                 | 255 us                                                      | 233 us: 1.09x faster                                        |
| nqueens                  | 67.0 ms                                                     | 61.6 ms: 1.09x faster                                       |
| unpickle                 | 9.17 us                                                     | 8.48 us: 1.08x faster                                       |
| dulwich_log              | 47.6 ms                                                     | 44.2 ms: 1.08x faster                                       |
| scimark_fft              | 193 ms                                                      | 180 ms: 1.08x faster                                        |
| sqlglot_normalize        | 202 ms                                                      | 188 ms: 1.07x faster                                        |
| regex_v8                 | 15.0 ms                                                     | 14.0 ms: 1.07x faster                                       |
| regex_dna                | 132 ms                                                      | 124 ms: 1.06x faster                                        |
| sqlite_synth             | 1.84 us                                                     | 1.73 us: 1.06x faster                                       |
| python_startup           | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.52 ms: 1.05x faster                                       |
| create_gc_cycles         | 782 us                                                      | 747 us: 1.05x faster                                        |
| json_loads               | 14.2 us                                                     | 13.6 us: 1.04x faster                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.09 us: 1.03x faster                                       |
| json                     | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.64 ms: 1.02x faster                                       |
| nbody                    | 69.3 ms                                                     | 70.1 ms: 1.01x slower                                       |
| meteor_contest           | 72.5 ms                                                     | 73.5 ms: 1.01x slower                                       |
| pidigits                 | 145 ms                                                      | 148 ms: 1.02x slower                                        |
| python_startup_no_site   | 15.5 ms                                                     | 15.9 ms: 1.03x slower                                       |
| unpack_sequence          | 37.8 ns                                                     | 39.0 ns: 1.03x slower                                       |
| xml_etree_generate       | 54.5 ms                                                     | 56.6 ms: 1.04x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.46 us: 1.04x slower                                       |
| logging_format           | 6.66 us                                                     | 7.00 us: 1.05x slower                                       |
| async_generators         | 224 ms                                                      | 235 ms: 1.05x slower                                        |
| pickle                   | 6.80 us                                                     | 7.24 us: 1.06x slower                                       |
| telco                    | 3.78 ms                                                     | 4.10 ms: 1.08x slower                                       |
| pathlib                  | 77.4 ms                                                     | 83.9 ms: 1.08x slower                                       |
| pickle_dict              | 16.9 us                                                     | 18.5 us: 1.09x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.88 us: 1.11x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 67.6 ms: 1.11x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.53 ms: 1.14x slower                                       |
| dask                     | 305 ms                                                      | 366 ms: 1.20x slower                                        |
| coverage                 | 40.0 ms                                                     | 51.2 ms: 1.28x slower                                       |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, xml_etree_iterparse, unpickle_list
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x
