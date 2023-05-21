
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 99b6418
- commit date: 2023-05-21
- overall geometric mean: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 209 ms: 1.13x faster                                        |
| docutils       | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                      |
| tornado_http   | 109 ms                                                      | 89.3 ms: 1.22x faster                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.6 ms: 1.12x faster                                       |
| nbody          | 69.3 ms                                                     | 70.2 ms: 1.01x slower                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 86.3 ms: 1.20x faster                                       |
| regex_v8       | 15.0 ms                                                     | 14.1 ms: 1.06x faster                                       |
| regex_dna      | 132 ms                                                      | 125 ms: 1.06x faster                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.59 ms: 1.52x faster                                       |
| pickle_pure_python   | 257 us                                                      | 193 us: 1.33x faster                                        |
| unpickle_pure_python | 171 us                                                      | 132 us: 1.30x faster                                        |
| tomli_loads          | 1.62 sec                                                    | 1.34 sec: 1.21x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 37.9 ms: 1.15x faster                                       |
| unpickle             | 9.17 us                                                     | 8.53 us: 1.08x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 94.7 ms: 1.07x faster                                       |
| json_loads           | 14.2 us                                                     | 13.8 us: 1.02x faster                                       |
| pickle               | 6.80 us                                                     | 6.95 us: 1.02x slower                                       |
| xml_etree_generate   | 54.5 ms                                                     | 56.0 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.5 ms: 1.03x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.1 us: 1.07x slower                                       |
| unpickle_list        | 2.81 us                                                     | 3.02 us: 1.07x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.88 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.3 ms: 1.04x faster                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.61 ms: 1.33x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf1-amd64-python-main-3.12.0a7+-99b6418 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 91.7 us: 3.54x faster                                       |
| deltablue                | 4.17 ms                                                     | 2.13 ms: 1.96x faster                                       |
| richards_super           | 51.7 ms                                                     | 29.3 ms: 1.77x faster                                       |
| mypy2                    | 352 ms                                                      | 215 ms: 1.64x faster                                        |
| logging_silent           | 96.4 ns                                                     | 60.1 ns: 1.60x faster                                       |
| richards                 | 41.2 ms                                                     | 25.7 ms: 1.60x faster                                       |
| go                       | 136 ms                                                      | 87.7 ms: 1.55x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 796 us: 1.53x faster                                        |
| async_tree_io            | 1.07 sec                                                    | 700 ms: 1.52x faster                                        |
| json_dumps               | 8.50 ms                                                     | 5.59 ms: 1.52x faster                                       |
| async_tree_none          | 420 ms                                                      | 282 ms: 1.49x faster                                        |
| async_tree_memoization   | 497 ms                                                      | 335 ms: 1.48x faster                                        |
| generators               | 31.6 ms                                                     | 21.5 ms: 1.47x faster                                       |
| scimark_lu               | 85.4 ms                                                     | 58.5 ms: 1.46x faster                                       |
| sqlglot_transpile        | 1.46 ms                                                     | 1.01 ms: 1.45x faster                                       |
| raytrace                 | 271 ms                                                      | 187 ms: 1.45x faster                                        |
| hexiom                   | 5.52 ms                                                     | 3.95 ms: 1.40x faster                                       |
| pyflate                  | 387 ms                                                      | 284 ms: 1.36x faster                                        |
| mako                     | 8.80 ms                                                     | 6.61 ms: 1.33x faster                                       |
| scimark_sor              | 105 ms                                                      | 78.9 ms: 1.33x faster                                       |
| pickle_pure_python       | 257 us                                                      | 193 us: 1.33x faster                                        |
| chaos                    | 58.9 ms                                                     | 44.4 ms: 1.33x faster                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.6 ms: 1.31x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 132 us: 1.30x faster                                        |
| crypto_pyaes             | 62.3 ms                                                     | 48.0 ms: 1.30x faster                                       |
| pycparser                | 868 ms                                                      | 673 ms: 1.29x faster                                        |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 474 ms: 1.29x faster                                        |
| mdp                      | 1.71 sec                                                    | 1.36 sec: 1.26x faster                                      |
| deepcopy_memo            | 28.5 us                                                     | 22.9 us: 1.25x faster                                       |
| asyncio_tcp              | 712 ms                                                      | 582 ms: 1.22x faster                                        |
| tornado_http             | 109 ms                                                      | 89.3 ms: 1.22x faster                                       |
| tomli_loads              | 1.62 sec                                                    | 1.34 sec: 1.21x faster                                      |
| spectral_norm            | 78.0 ms                                                     | 64.8 ms: 1.20x faster                                       |
| regex_compile            | 103 ms                                                      | 86.3 ms: 1.20x faster                                       |
| pprint_pformat           | 1.21 sec                                                    | 1.02 sec: 1.18x faster                                      |
| docutils                 | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 509 ms: 1.16x faster                                        |
| coroutines               | 15.9 ms                                                     | 13.9 ms: 1.15x faster                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 34.0 ms: 1.15x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 37.9 ms: 1.15x faster                                       |
| aiohttp                  | 1.01 ms                                                     | 886 us: 1.14x faster                                        |
| bench_thread_pool        | 946 us                                                      | 834 us: 1.13x faster                                        |
| 2to3                     | 237 ms                                                      | 209 ms: 1.13x faster                                        |
| comprehensions           | 16.0 us                                                     | 14.1 us: 1.13x faster                                       |
| create_gc_cycles         | 782 us                                                      | 694 us: 1.13x faster                                        |
| float                    | 60.2 ms                                                     | 53.6 ms: 1.12x faster                                       |
| nqueens                  | 67.0 ms                                                     | 60.2 ms: 1.11x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 182 ms: 1.11x faster                                        |
| dulwich_log              | 47.6 ms                                                     | 42.9 ms: 1.11x faster                                       |
| deepcopy                 | 255 us                                                      | 230 us: 1.11x faster                                        |
| scimark_fft              | 193 ms                                                      | 176 ms: 1.10x faster                                        |
| sqlite_synth             | 1.84 us                                                     | 1.69 us: 1.09x faster                                       |
| unpickle                 | 9.17 us                                                     | 8.53 us: 1.08x faster                                       |
| xml_etree_parse          | 102 ms                                                      | 94.7 ms: 1.07x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.48 ms: 1.07x faster                                       |
| fannkuch                 | 258 ms                                                      | 242 ms: 1.06x faster                                        |
| regex_v8                 | 15.0 ms                                                     | 14.1 ms: 1.06x faster                                       |
| regex_dna                | 132 ms                                                      | 125 ms: 1.06x faster                                        |
| python_startup           | 20.0 ms                                                     | 19.3 ms: 1.04x faster                                       |
| json                     | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.10 us: 1.03x faster                                       |
| json_loads               | 14.2 us                                                     | 13.8 us: 1.02x faster                                       |
| meteor_contest           | 72.5 ms                                                     | 72.3 ms: 1.00x faster                                       |
| nbody                    | 69.3 ms                                                     | 70.2 ms: 1.01x slower                                       |
| pickle                   | 6.80 us                                                     | 6.95 us: 1.02x slower                                       |
| xml_etree_generate       | 54.5 ms                                                     | 56.0 ms: 1.03x slower                                       |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.5 ms: 1.03x slower                                       |
| async_generators         | 224 ms                                                      | 231 ms: 1.03x slower                                        |
| pidigits                 | 145 ms                                                      | 151 ms: 1.04x slower                                        |
| python_startup_no_site   | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.57 us: 1.06x slower                                       |
| logging_format           | 6.66 us                                                     | 7.09 us: 1.06x slower                                       |
| pickle_dict              | 16.9 us                                                     | 18.1 us: 1.07x slower                                       |
| unpickle_list            | 2.81 us                                                     | 3.02 us: 1.07x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.45 ms: 1.08x slower                                       |
| telco                    | 3.78 ms                                                     | 4.08 ms: 1.08x slower                                       |
| pathlib                  | 77.4 ms                                                     | 85.3 ms: 1.10x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.88 us: 1.11x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 68.4 ms: 1.13x slower                                       |
| dask                     | 305 ms                                                      | 366 ms: 1.20x slower                                        |
| coverage                 | 40.0 ms                                                     | 50.4 ms: 1.26x slower                                       |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, regex_effbot, unpack_sequence
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
