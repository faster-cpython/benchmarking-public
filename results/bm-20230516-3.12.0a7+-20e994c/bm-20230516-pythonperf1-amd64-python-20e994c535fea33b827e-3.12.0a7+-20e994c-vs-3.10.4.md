
# Results vs. 3.10.4

- fork: python
- ref: 20e994c535fea33b827e
- machine: windows-amd64
- commit hash: 20e994c
- commit date: 2023-05-16
- overall geometric mean: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 214 ms: 1.11x faster                                                        |
| docutils       | 1.89 sec                                                    | 1.61 sec: 1.17x faster                                                      |
| tornado_http   | 109 ms                                                      | 88.4 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 55.9 ms: 1.08x faster                                                       |
| pidigits       | 145 ms                                                      | 149 ms: 1.03x slower                                                        |
| nbody          | 69.3 ms                                                     | 76.5 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 87.4 ms: 1.18x faster                                                       |
| regex_dna      | 132 ms                                                      | 118 ms: 1.12x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 13.7 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.82 ms: 1.46x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 198 us: 1.30x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 138 us: 1.24x faster                                                        |
| tomli_loads          | 1.62 sec                                                    | 1.43 sec: 1.13x faster                                                      |
| unpickle             | 9.17 us                                                     | 8.33 us: 1.10x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 93.0 ms: 1.09x faster                                                       |
| xml_etree_process    | 43.4 ms                                                     | 40.2 ms: 1.08x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.03x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.88 us: 1.03x slower                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.8 ms: 1.04x slower                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 57.2 ms: 1.05x slower                                                       |
| pickle               | 6.80 us                                                     | 7.15 us: 1.05x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.1 us: 1.07x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.85 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.92 ms: 1.27x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230516-pythonperf1-amd64-python-20e994c535fea33b827e-3.12.0a7+-20e994c |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 105 us: 3.10x faster                                                        |
| deltablue                | 4.17 ms                                                     | 2.21 ms: 1.89x faster                                                       |
| richards_super           | 51.7 ms                                                     | 31.2 ms: 1.66x faster                                                       |
| mypy2                    | 352 ms                                                      | 215 ms: 1.63x faster                                                        |
| logging_silent           | 96.4 ns                                                     | 60.9 ns: 1.58x faster                                                       |
| go                       | 136 ms                                                      | 89.4 ms: 1.52x faster                                                       |
| richards                 | 41.2 ms                                                     | 27.4 ms: 1.50x faster                                                       |
| async_tree_memoization   | 497 ms                                                      | 331 ms: 1.50x faster                                                        |
| async_tree_io            | 1.07 sec                                                    | 718 ms: 1.48x faster                                                        |
| async_tree_none          | 420 ms                                                      | 286 ms: 1.47x faster                                                        |
| asyncio_tcp              | 712 ms                                                      | 486 ms: 1.47x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 834 us: 1.46x faster                                                        |
| json_dumps               | 8.50 ms                                                     | 5.82 ms: 1.46x faster                                                       |
| scimark_lu               | 85.4 ms                                                     | 59.2 ms: 1.44x faster                                                       |
| raytrace                 | 271 ms                                                      | 191 ms: 1.42x faster                                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 1.05 ms: 1.40x faster                                                       |
| generators               | 31.6 ms                                                     | 22.9 ms: 1.38x faster                                                       |
| chaos                    | 58.9 ms                                                     | 44.4 ms: 1.33x faster                                                       |
| crypto_pyaes             | 62.3 ms                                                     | 48.0 ms: 1.30x faster                                                       |
| pickle_pure_python       | 257 us                                                      | 198 us: 1.30x faster                                                        |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 471 ms: 1.29x faster                                                        |
| hexiom                   | 5.52 ms                                                     | 4.31 ms: 1.28x faster                                                       |
| mako                     | 8.80 ms                                                     | 6.92 ms: 1.27x faster                                                       |
| pyflate                  | 387 ms                                                      | 305 ms: 1.27x faster                                                        |
| pycparser                | 868 ms                                                      | 692 ms: 1.25x faster                                                        |
| scimark_monte_carlo      | 55.9 ms                                                     | 44.7 ms: 1.25x faster                                                       |
| unpickle_pure_python     | 171 us                                                      | 138 us: 1.24x faster                                                        |
| tornado_http             | 109 ms                                                      | 88.4 ms: 1.23x faster                                                       |
| scimark_sor              | 105 ms                                                      | 85.1 ms: 1.23x faster                                                       |
| spectral_norm            | 78.0 ms                                                     | 65.0 ms: 1.20x faster                                                       |
| regex_compile            | 103 ms                                                      | 87.4 ms: 1.18x faster                                                       |
| mdp                      | 1.71 sec                                                    | 1.45 sec: 1.18x faster                                                      |
| docutils                 | 1.89 sec                                                    | 1.61 sec: 1.17x faster                                                      |
| deepcopy_memo            | 28.5 us                                                     | 25.1 us: 1.14x faster                                                       |
| tomli_loads              | 1.62 sec                                                    | 1.43 sec: 1.13x faster                                                      |
| dulwich_log              | 47.6 ms                                                     | 42.4 ms: 1.12x faster                                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 34.7 ms: 1.12x faster                                                       |
| regex_dna                | 132 ms                                                      | 118 ms: 1.12x faster                                                        |
| create_gc_cycles         | 782 us                                                      | 699 us: 1.12x faster                                                        |
| aiohttp                  | 1.01 ms                                                     | 904 us: 1.11x faster                                                        |
| bench_thread_pool        | 946 us                                                      | 853 us: 1.11x faster                                                        |
| 2to3                     | 237 ms                                                      | 214 ms: 1.11x faster                                                        |
| unpickle                 | 9.17 us                                                     | 8.33 us: 1.10x faster                                                       |
| regex_v8                 | 15.0 ms                                                     | 13.7 ms: 1.10x faster                                                       |
| pprint_pformat           | 1.21 sec                                                    | 1.10 sec: 1.10x faster                                                      |
| coroutines               | 15.9 ms                                                     | 14.5 ms: 1.10x faster                                                       |
| sqlglot_normalize        | 202 ms                                                      | 184 ms: 1.10x faster                                                        |
| xml_etree_parse          | 102 ms                                                      | 93.0 ms: 1.09x faster                                                       |
| comprehensions           | 16.0 us                                                     | 14.6 us: 1.09x faster                                                       |
| pprint_safe_repr         | 589 ms                                                      | 539 ms: 1.09x faster                                                        |
| sqlite_synth             | 1.84 us                                                     | 1.70 us: 1.08x faster                                                       |
| xml_etree_process        | 43.4 ms                                                     | 40.2 ms: 1.08x faster                                                       |
| nqueens                  | 67.0 ms                                                     | 62.2 ms: 1.08x faster                                                       |
| float                    | 60.2 ms                                                     | 55.9 ms: 1.08x faster                                                       |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.89 sec: 1.07x faster                                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.50 ms: 1.06x faster                                                       |
| deepcopy                 | 255 us                                                      | 242 us: 1.06x faster                                                        |
| fannkuch                 | 258 ms                                                      | 245 ms: 1.05x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                       |
| python_startup           | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                                       |
| scimark_fft              | 193 ms                                                      | 187 ms: 1.03x faster                                                        |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.03x faster                                                       |
| json                     | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                                       |
| pidigits                 | 145 ms                                                      | 149 ms: 1.03x slower                                                        |
| unpickle_list            | 2.81 us                                                     | 2.88 us: 1.03x slower                                                       |
| meteor_contest           | 72.5 ms                                                     | 75.1 ms: 1.03x slower                                                       |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.8 ms: 1.04x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                                       |
| async_generators         | 224 ms                                                      | 235 ms: 1.05x slower                                                        |
| xml_etree_generate       | 54.5 ms                                                     | 57.2 ms: 1.05x slower                                                       |
| pickle                   | 6.80 us                                                     | 7.15 us: 1.05x slower                                                       |
| pathlib                  | 77.4 ms                                                     | 82.0 ms: 1.06x slower                                                       |
| telco                    | 3.78 ms                                                     | 4.02 ms: 1.06x slower                                                       |
| logging_format           | 6.66 us                                                     | 7.11 us: 1.07x slower                                                       |
| pickle_dict              | 16.9 us                                                     | 18.1 us: 1.07x slower                                                       |
| logging_simple           | 6.20 us                                                     | 6.65 us: 1.07x slower                                                       |
| unpack_sequence          | 37.8 ns                                                     | 41.4 ns: 1.10x slower                                                       |
| gc_traversal             | 1.34 ms                                                     | 1.47 ms: 1.10x slower                                                       |
| pickle_list              | 2.59 us                                                     | 2.85 us: 1.10x slower                                                       |
| nbody                    | 69.3 ms                                                     | 76.5 ms: 1.10x slower                                                       |
| bench_mp_pool            | 60.7 ms                                                     | 67.9 ms: 1.12x slower                                                       |
| dask                     | 305 ms                                                      | 364 ms: 1.19x slower                                                        |
| coverage                 | 40.0 ms                                                     | 50.4 ms: 1.26x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (1): deepcopy_reduce
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
