
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 30c127f
- commit date: 2023-07-15
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 210 ms: 1.13x faster                                        |
| docutils       | 1.89 sec                                                    | 1.61 sec: 1.18x faster                                      |
| tornado_http   | 109 ms                                                      | 86.4 ms: 1.26x faster                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.3 ms: 1.13x faster                                       |
| nbody          | 69.3 ms                                                     | 70.6 ms: 1.02x slower                                       |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 87.4 ms: 1.18x faster                                       |
| regex_dna      | 132 ms                                                      | 119 ms: 1.11x faster                                        |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.71 ms: 1.49x faster                                       |
| pickle_pure_python   | 257 us                                                      | 196 us: 1.31x faster                                        |
| unpickle_pure_python | 171 us                                                      | 134 us: 1.28x faster                                        |
| tomli_loads          | 1.62 sec                                                    | 1.38 sec: 1.17x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 38.0 ms: 1.14x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 89.3 ms: 1.14x faster                                       |
| unpickle             | 9.17 us                                                     | 8.19 us: 1.12x faster                                       |
| json_loads           | 14.2 us                                                     | 13.6 us: 1.04x faster                                       |
| xml_etree_generate   | 54.5 ms                                                     | 55.1 ms: 1.01x slower                                       |
| pickle               | 6.80 us                                                     | 7.03 us: 1.03x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.3 us: 1.08x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.84 us: 1.10x slower                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.6 ms: 1.08x faster                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.65 ms: 1.32x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.7 us: 3.39x faster                                       |
| deltablue                | 4.17 ms                                                     | 2.10 ms: 1.99x faster                                       |
| richards_super           | 51.7 ms                                                     | 30.6 ms: 1.69x faster                                       |
| mypy2                    | 352 ms                                                      | 209 ms: 1.68x faster                                        |
| logging_silent           | 96.4 ns                                                     | 61.4 ns: 1.57x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 694 ms: 1.54x faster                                        |
| go                       | 136 ms                                                      | 89.4 ms: 1.52x faster                                       |
| richards                 | 41.2 ms                                                     | 27.1 ms: 1.52x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 330 ms: 1.51x faster                                        |
| sqlglot_parse            | 1.22 ms                                                     | 813 us: 1.50x faster                                        |
| asyncio_tcp              | 712 ms                                                      | 477 ms: 1.49x faster                                        |
| json_dumps               | 8.50 ms                                                     | 5.71 ms: 1.49x faster                                       |
| async_tree_none          | 420 ms                                                      | 284 ms: 1.48x faster                                        |
| raytrace                 | 271 ms                                                      | 186 ms: 1.46x faster                                        |
| scimark_lu               | 85.4 ms                                                     | 59.7 ms: 1.43x faster                                       |
| generators               | 31.6 ms                                                     | 22.1 ms: 1.43x faster                                       |
| sqlglot_transpile        | 1.46 ms                                                     | 1.02 ms: 1.43x faster                                       |
| chaos                    | 58.9 ms                                                     | 43.2 ms: 1.36x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.14 ms: 1.33x faster                                       |
| mako                     | 8.80 ms                                                     | 6.65 ms: 1.32x faster                                       |
| pickle_pure_python       | 257 us                                                      | 196 us: 1.31x faster                                        |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 468 ms: 1.30x faster                                        |
| pycparser                | 868 ms                                                      | 668 ms: 1.30x faster                                        |
| pyflate                  | 387 ms                                                      | 300 ms: 1.29x faster                                        |
| unpickle_pure_python     | 171 us                                                      | 134 us: 1.28x faster                                        |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.8 ms: 1.28x faster                                       |
| crypto_pyaes             | 62.3 ms                                                     | 48.9 ms: 1.27x faster                                       |
| tornado_http             | 109 ms                                                      | 86.4 ms: 1.26x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.36 sec: 1.26x faster                                      |
| scimark_sor              | 105 ms                                                      | 83.9 ms: 1.25x faster                                       |
| aiohttp                  | 1.01 ms                                                     | 847 us: 1.19x faster                                        |
| regex_compile            | 103 ms                                                      | 87.4 ms: 1.18x faster                                       |
| docutils                 | 1.89 sec                                                    | 1.61 sec: 1.18x faster                                      |
| tomli_loads              | 1.62 sec                                                    | 1.38 sec: 1.17x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.04 sec: 1.16x faster                                      |
| deepcopy_memo            | 28.5 us                                                     | 24.6 us: 1.16x faster                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 33.6 ms: 1.16x faster                                       |
| pprint_safe_repr         | 589 ms                                                      | 511 ms: 1.15x faster                                        |
| xml_etree_process        | 43.4 ms                                                     | 38.0 ms: 1.14x faster                                       |
| spectral_norm            | 78.0 ms                                                     | 68.3 ms: 1.14x faster                                       |
| bench_thread_pool        | 946 us                                                      | 831 us: 1.14x faster                                        |
| xml_etree_parse          | 102 ms                                                      | 89.3 ms: 1.14x faster                                       |
| comprehensions           | 16.0 us                                                     | 14.1 us: 1.13x faster                                       |
| coroutines               | 15.9 ms                                                     | 14.1 ms: 1.13x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 179 ms: 1.13x faster                                        |
| float                    | 60.2 ms                                                     | 53.3 ms: 1.13x faster                                       |
| 2to3                     | 237 ms                                                      | 210 ms: 1.13x faster                                        |
| unpickle                 | 9.17 us                                                     | 8.19 us: 1.12x faster                                       |
| dulwich_log              | 47.6 ms                                                     | 42.5 ms: 1.12x faster                                       |
| regex_dna                | 132 ms                                                      | 119 ms: 1.11x faster                                        |
| nqueens                  | 67.0 ms                                                     | 60.9 ms: 1.10x faster                                       |
| regex_v8                 | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                       |
| create_gc_cycles         | 782 us                                                      | 722 us: 1.08x faster                                        |
| python_startup           | 20.0 ms                                                     | 18.6 ms: 1.08x faster                                       |
| deepcopy                 | 255 us                                                      | 238 us: 1.07x faster                                        |
| scimark_fft              | 193 ms                                                      | 181 ms: 1.07x faster                                        |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.92 sec: 1.06x faster                                      |
| sqlite_synth             | 1.84 us                                                     | 1.74 us: 1.06x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.53 ms: 1.05x faster                                       |
| json                     | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                       |
| json_loads               | 14.2 us                                                     | 13.6 us: 1.04x faster                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.11 us: 1.02x faster                                       |
| fannkuch                 | 258 ms                                                      | 253 ms: 1.02x faster                                        |
| xml_etree_generate       | 54.5 ms                                                     | 55.1 ms: 1.01x slower                                       |
| async_generators         | 224 ms                                                      | 227 ms: 1.02x slower                                        |
| meteor_contest           | 72.5 ms                                                     | 73.9 ms: 1.02x slower                                       |
| nbody                    | 69.3 ms                                                     | 70.6 ms: 1.02x slower                                       |
| pathlib                  | 77.4 ms                                                     | 79.1 ms: 1.02x slower                                       |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                        |
| pickle                   | 6.80 us                                                     | 7.03 us: 1.03x slower                                       |
| unpack_sequence          | 37.8 ns                                                     | 39.3 ns: 1.04x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.47 us: 1.04x slower                                       |
| logging_format           | 6.66 us                                                     | 6.97 us: 1.05x slower                                       |
| telco                    | 3.78 ms                                                     | 4.05 ms: 1.07x slower                                       |
| pickle_dict              | 16.9 us                                                     | 18.3 us: 1.08x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.46 ms: 1.09x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.84 us: 1.10x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 67.0 ms: 1.10x slower                                       |
| dask                     | 305 ms                                                      | 362 ms: 1.19x slower                                        |
| coverage                 | 40.0 ms                                                     | 50.7 ms: 1.27x slower                                       |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, python_startup_no_site, unpickle_list
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x
