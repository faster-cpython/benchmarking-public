
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 7d2deaf
- commit date: 2023-05-13
- overall geometric mean: 1.06x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                      |
| tornado_http   | 91.8 ms                                                     | 87.1 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 53.3 ms: 1.03x faster                                       |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                        |
| nbody          | 70.0 ms                                                     | 71.6 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 87.1 ms: 1.04x faster                                       |
| regex_v8       | 13.8 ms                                                     | 13.5 ms: 1.02x faster                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.73 ms: 1.32x faster                                       |
| unpickle_pure_python | 152 us                                                      | 135 us: 1.12x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 89.1 ms: 1.08x faster                                       |
| pickle_pure_python   | 200 us                                                      | 192 us: 1.04x faster                                        |
| tomli_loads          | 1.41 sec                                                    | 1.40 sec: 1.01x faster                                      |
| unpickle             | 8.09 us                                                     | 8.18 us: 1.01x slower                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.6 ms: 1.02x slower                                       |
| xml_etree_process    | 37.1 ms                                                     | 38.3 ms: 1.03x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 54.8 ms: 1.05x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.83 us: 1.06x slower                                       |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                       |
| pickle               | 6.61 us                                                     | 7.05 us: 1.07x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.96 us: 1.16x slower                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.1 ms: 1.02x slower                                       |
| python_startup         | 18.7 ms                                                     | 19.2 ms: 1.02x slower                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.60 ms: 1.10x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-pythonperf1-amd64-python-main-3.12.0a7+-7d2deaf |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 98.7 us: 3.26x faster                                       |
| generators               | 33.8 ms                                                     | 21.9 ms: 1.54x faster                                       |
| asyncio_tcp              | 699 ms                                                      | 486 ms: 1.44x faster                                        |
| json_dumps               | 7.56 ms                                                     | 5.73 ms: 1.32x faster                                       |
| unpack_sequence          | 46.1 ns                                                     | 35.3 ns: 1.30x faster                                       |
| deltablue                | 2.61 ms                                                     | 2.08 ms: 1.25x faster                                       |
| richards_super           | 37.5 ms                                                     | 30.4 ms: 1.23x faster                                       |
| mdp                      | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                      |
| sqlglot_parse            | 952 us                                                      | 786 us: 1.21x faster                                        |
| logging_silent           | 69.8 ns                                                     | 58.9 ns: 1.18x faster                                       |
| richards                 | 30.6 ms                                                     | 26.0 ms: 1.18x faster                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.01 ms: 1.15x faster                                       |
| comprehensions           | 15.9 us                                                     | 13.9 us: 1.14x faster                                       |
| go                       | 97.3 ms                                                     | 85.6 ms: 1.14x faster                                       |
| hexiom                   | 4.55 ms                                                     | 4.01 ms: 1.14x faster                                       |
| json                     | 3.25 ms                                                     | 2.87 ms: 1.13x faster                                       |
| raytrace                 | 211 ms                                                      | 187 ms: 1.13x faster                                        |
| unpickle_pure_python     | 152 us                                                      | 135 us: 1.12x faster                                        |
| async_tree_none          | 320 ms                                                      | 285 ms: 1.12x faster                                        |
| chaos                    | 47.1 ms                                                     | 42.3 ms: 1.11x faster                                       |
| nqueens                  | 64.9 ms                                                     | 58.4 ms: 1.11x faster                                       |
| async_tree_memoization   | 371 ms                                                      | 334 ms: 1.11x faster                                        |
| mako                     | 7.26 ms                                                     | 6.60 ms: 1.10x faster                                       |
| coverage                 | 55.9 ms                                                     | 50.9 ms: 1.10x faster                                       |
| xml_etree_parse          | 95.9 ms                                                     | 89.1 ms: 1.08x faster                                       |
| mypy2                    | 229 ms                                                      | 213 ms: 1.08x faster                                        |
| scimark_lu               | 63.5 ms                                                     | 59.1 ms: 1.07x faster                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.96 sec: 1.07x faster                                      |
| spectral_norm            | 67.9 ms                                                     | 63.2 ms: 1.07x faster                                       |
| async_tree_io            | 779 ms                                                      | 725 ms: 1.07x faster                                        |
| dulwich_log              | 44.5 ms                                                     | 41.7 ms: 1.07x faster                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 471 ms: 1.06x faster                                        |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.42 ms: 1.06x faster                                       |
| deepcopy                 | 246 us                                                      | 233 us: 1.05x faster                                        |
| tornado_http             | 91.8 ms                                                     | 87.1 ms: 1.05x faster                                       |
| deepcopy_memo            | 25.2 us                                                     | 24.1 us: 1.05x faster                                       |
| logging_simple           | 6.61 us                                                     | 6.36 us: 1.04x faster                                       |
| regex_compile            | 90.6 ms                                                     | 87.1 ms: 1.04x faster                                       |
| pickle_pure_python       | 200 us                                                      | 192 us: 1.04x faster                                        |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.9 ms: 1.04x faster                                       |
| pyflate                  | 304 ms                                                      | 293 ms: 1.04x faster                                        |
| sqlglot_normalize        | 190 ms                                                      | 185 ms: 1.03x faster                                        |
| crypto_pyaes             | 47.6 ms                                                     | 46.3 ms: 1.03x faster                                       |
| float                    | 54.6 ms                                                     | 53.3 ms: 1.03x faster                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 34.0 ms: 1.03x faster                                       |
| bench_thread_pool        | 852 us                                                      | 831 us: 1.03x faster                                        |
| coroutines               | 14.6 ms                                                     | 14.3 ms: 1.03x faster                                       |
| logging_format           | 7.01 us                                                     | 6.84 us: 1.02x faster                                       |
| pycparser                | 691 ms                                                      | 675 ms: 1.02x faster                                        |
| regex_v8                 | 13.8 ms                                                     | 13.5 ms: 1.02x faster                                       |
| fannkuch                 | 252 ms                                                      | 247 ms: 1.02x faster                                        |
| aiohttp                  | 899 us                                                      | 887 us: 1.01x faster                                        |
| tomli_loads              | 1.41 sec                                                    | 1.40 sec: 1.01x faster                                      |
| pprint_safe_repr         | 512 ms                                                      | 515 ms: 1.01x slower                                        |
| pidigits                 | 148 ms                                                      | 149 ms: 1.01x slower                                        |
| docutils                 | 1.60 sec                                                    | 1.62 sec: 1.01x slower                                      |
| sqlite_synth             | 1.68 us                                                     | 1.70 us: 1.01x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.18 us: 1.01x slower                                       |
| regex_dna                | 115 ms                                                      | 117 ms: 1.01x slower                                        |
| pprint_pformat           | 1.04 sec                                                    | 1.05 sec: 1.01x slower                                      |
| python_startup_no_site   | 15.9 ms                                                     | 16.1 ms: 1.02x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 63.6 ms: 1.02x slower                                       |
| gc_traversal             | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                       |
| nbody                    | 70.0 ms                                                     | 71.6 ms: 1.02x slower                                       |
| python_startup           | 18.7 ms                                                     | 19.2 ms: 1.02x slower                                       |
| create_gc_cycles         | 693 us                                                      | 710 us: 1.02x slower                                        |
| telco                    | 3.90 ms                                                     | 4.04 ms: 1.03x slower                                       |
| xml_etree_process        | 37.1 ms                                                     | 38.3 ms: 1.03x slower                                       |
| scimark_sor              | 75.6 ms                                                     | 78.4 ms: 1.04x slower                                       |
| xml_etree_generate       | 52.2 ms                                                     | 54.8 ms: 1.05x slower                                       |
| regex_effbot             | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.83 us: 1.06x slower                                       |
| bench_mp_pool            | 62.5 ms                                                     | 66.4 ms: 1.06x slower                                       |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                       |
| pickle                   | 6.61 us                                                     | 7.05 us: 1.07x slower                                       |
| pathlib                  | 71.4 ms                                                     | 80.9 ms: 1.13x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.96 us: 1.16x slower                                       |
| async_generators         | 178 ms                                                      | 237 ms: 1.33x slower                                        |
| dask                     | 264 ms                                                      | 363 ms: 1.37x slower                                        |
| Geometric mean           | (ref)                                                       | 1.06x faster                                                |

Benchmark hidden because not significant (5): pickle_dict, scimark_fft, meteor_contest, 2to3, deepcopy_reduce
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
