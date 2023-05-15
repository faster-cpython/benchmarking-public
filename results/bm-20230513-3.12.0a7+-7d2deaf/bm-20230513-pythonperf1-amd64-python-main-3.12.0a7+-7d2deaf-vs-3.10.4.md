
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 7d2deaf
- commit date: 2023-05-13
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 209 ms: 1.13x faster                                        |
| docutils       | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                      |
| tornado_http   | 109 ms                                                      | 87.1 ms: 1.25x faster                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.3 ms: 1.13x faster                                       |
| pidigits       | 145 ms                                                      | 149 ms: 1.03x slower                                        |
| nbody          | 69.3 ms                                                     | 71.6 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 87.1 ms: 1.19x faster                                       |
| regex_dna      | 132 ms                                                      | 117 ms: 1.13x faster                                        |
| regex_v8       | 15.0 ms                                                     | 13.5 ms: 1.11x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.73 ms: 1.48x faster                                       |
| pickle_pure_python   | 257 us                                                      | 192 us: 1.34x faster                                        |
| unpickle_pure_python | 171 us                                                      | 135 us: 1.27x faster                                        |
| tomli_loads          | 1.62 sec                                                    | 1.40 sec: 1.16x faster                                      |
| xml_etree_parse      | 102 ms                                                      | 89.1 ms: 1.14x faster                                       |
| xml_etree_process    | 43.4 ms                                                     | 38.3 ms: 1.13x faster                                       |
| unpickle             | 9.17 us                                                     | 8.18 us: 1.12x faster                                       |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.03x faster                                       |
| xml_etree_generate   | 54.5 ms                                                     | 54.8 ms: 1.00x slower                                       |
| pickle               | 6.80 us                                                     | 7.05 us: 1.04x slower                                       |
| unpickle_list        | 2.81 us                                                     | 2.96 us: 1.05x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.4 us: 1.09x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.83 us: 1.09x slower                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.1 ms: 1.04x slower                                       |
| Geometric mean         | (ref)                                                       | 1.00x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.60 ms: 1.33x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 98.7 us: 3.29x faster                                       |
| deltablue                | 4.17 ms                                                     | 2.08 ms: 2.00x faster                                       |
| richards_super           | 51.7 ms                                                     | 30.4 ms: 1.70x faster                                       |
| mypy2                    | 352 ms                                                      | 213 ms: 1.65x faster                                        |
| logging_silent           | 96.4 ns                                                     | 58.9 ns: 1.64x faster                                       |
| go                       | 136 ms                                                      | 85.6 ms: 1.59x faster                                       |
| richards                 | 41.2 ms                                                     | 26.0 ms: 1.59x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 786 us: 1.55x faster                                        |
| async_tree_memoization   | 497 ms                                                      | 334 ms: 1.49x faster                                        |
| json_dumps               | 8.50 ms                                                     | 5.73 ms: 1.48x faster                                       |
| async_tree_none          | 420 ms                                                      | 285 ms: 1.47x faster                                        |
| async_tree_io            | 1.07 sec                                                    | 725 ms: 1.47x faster                                        |
| asyncio_tcp              | 712 ms                                                      | 486 ms: 1.47x faster                                        |
| raytrace                 | 271 ms                                                      | 187 ms: 1.45x faster                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 1.01 ms: 1.45x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 59.1 ms: 1.45x faster                                       |
| generators               | 31.6 ms                                                     | 21.9 ms: 1.44x faster                                       |
| chaos                    | 58.9 ms                                                     | 42.3 ms: 1.39x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.01 ms: 1.38x faster                                       |
| crypto_pyaes             | 62.3 ms                                                     | 46.3 ms: 1.35x faster                                       |
| scimark_sor              | 105 ms                                                      | 78.4 ms: 1.34x faster                                       |
| pickle_pure_python       | 257 us                                                      | 192 us: 1.34x faster                                        |
| mako                     | 8.80 ms                                                     | 6.60 ms: 1.33x faster                                       |
| pyflate                  | 387 ms                                                      | 293 ms: 1.32x faster                                        |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.9 ms: 1.30x faster                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 471 ms: 1.29x faster                                        |
| pycparser                | 868 ms                                                      | 675 ms: 1.29x faster                                        |
| unpickle_pure_python     | 171 us                                                      | 135 us: 1.27x faster                                        |
| mdp                      | 1.71 sec                                                    | 1.36 sec: 1.26x faster                                      |
| tornado_http             | 109 ms                                                      | 87.1 ms: 1.25x faster                                       |
| spectral_norm            | 78.0 ms                                                     | 63.2 ms: 1.23x faster                                       |
| regex_compile            | 103 ms                                                      | 87.1 ms: 1.19x faster                                       |
| deepcopy_memo            | 28.5 us                                                     | 24.1 us: 1.19x faster                                       |
| docutils                 | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                      |
| tomli_loads              | 1.62 sec                                                    | 1.40 sec: 1.16x faster                                      |
| nqueens                  | 67.0 ms                                                     | 58.4 ms: 1.15x faster                                       |
| comprehensions           | 16.0 us                                                     | 13.9 us: 1.15x faster                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 34.0 ms: 1.15x faster                                       |
| pprint_pformat           | 1.21 sec                                                    | 1.05 sec: 1.14x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 515 ms: 1.14x faster                                        |
| xml_etree_parse          | 102 ms                                                      | 89.1 ms: 1.14x faster                                       |
| dulwich_log              | 47.6 ms                                                     | 41.7 ms: 1.14x faster                                       |
| bench_thread_pool        | 946 us                                                      | 831 us: 1.14x faster                                        |
| aiohttp                  | 1.01 ms                                                     | 887 us: 1.14x faster                                        |
| xml_etree_process        | 43.4 ms                                                     | 38.3 ms: 1.13x faster                                       |
| 2to3                     | 237 ms                                                      | 209 ms: 1.13x faster                                        |
| float                    | 60.2 ms                                                     | 53.3 ms: 1.13x faster                                       |
| regex_dna                | 132 ms                                                      | 117 ms: 1.13x faster                                        |
| unpickle                 | 9.17 us                                                     | 8.18 us: 1.12x faster                                       |
| coroutines               | 15.9 ms                                                     | 14.3 ms: 1.12x faster                                       |
| regex_v8                 | 15.0 ms                                                     | 13.5 ms: 1.11x faster                                       |
| create_gc_cycles         | 782 us                                                      | 710 us: 1.10x faster                                        |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.42 ms: 1.10x faster                                       |
| deepcopy                 | 255 us                                                      | 233 us: 1.10x faster                                        |
| sqlglot_normalize        | 202 ms                                                      | 185 ms: 1.10x faster                                        |
| scimark_fft              | 193 ms                                                      | 178 ms: 1.09x faster                                        |
| sqlite_synth             | 1.84 us                                                     | 1.70 us: 1.08x faster                                       |
| unpack_sequence          | 37.8 ns                                                     | 35.3 ns: 1.07x faster                                       |
| json                     | 3.05 ms                                                     | 2.87 ms: 1.06x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                       |
| python_startup           | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                       |
| fannkuch                 | 258 ms                                                      | 247 ms: 1.04x faster                                        |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.96 sec: 1.04x faster                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.09 us: 1.03x faster                                       |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.03x faster                                       |
| xml_etree_generate       | 54.5 ms                                                     | 54.8 ms: 1.00x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.36 us: 1.03x slower                                       |
| logging_format           | 6.66 us                                                     | 6.84 us: 1.03x slower                                       |
| meteor_contest           | 72.5 ms                                                     | 74.6 ms: 1.03x slower                                       |
| pidigits                 | 145 ms                                                      | 149 ms: 1.03x slower                                        |
| nbody                    | 69.3 ms                                                     | 71.6 ms: 1.03x slower                                       |
| pickle                   | 6.80 us                                                     | 7.05 us: 1.04x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.1 ms: 1.04x slower                                       |
| pathlib                  | 77.4 ms                                                     | 80.9 ms: 1.05x slower                                       |
| unpickle_list            | 2.81 us                                                     | 2.96 us: 1.05x slower                                       |
| async_generators         | 224 ms                                                      | 237 ms: 1.06x slower                                        |
| telco                    | 3.78 ms                                                     | 4.04 ms: 1.07x slower                                       |
| pickle_dict              | 16.9 us                                                     | 18.4 us: 1.09x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 66.4 ms: 1.09x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.83 us: 1.09x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                       |
| dask                     | 305 ms                                                      | 363 ms: 1.19x slower                                        |
| coverage                 | 40.0 ms                                                     | 50.9 ms: 1.27x slower                                       |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
