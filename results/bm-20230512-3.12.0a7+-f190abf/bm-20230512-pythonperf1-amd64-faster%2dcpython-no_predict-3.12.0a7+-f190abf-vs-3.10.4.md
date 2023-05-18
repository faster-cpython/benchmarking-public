
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_predict
- machine: windows-amd64
- commit hash: f190abf
- commit date: 2023-05-12
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 206 ms: 1.15x faster                                                        |
| docutils       | 1.89 sec                                                    | 1.61 sec: 1.18x faster                                                      |
| tornado_http   | 109 ms                                                      | 89.5 ms: 1.22x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 51.6 ms: 1.17x faster                                                       |
| nbody          | 69.3 ms                                                     | 68.3 ms: 1.01x faster                                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 84.2 ms: 1.23x faster                                                       |
| regex_dna      | 132 ms                                                      | 120 ms: 1.10x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.69 ms: 1.49x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 187 us: 1.37x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 130 us: 1.32x faster                                                        |
| tomli_loads          | 1.62 sec                                                    | 1.32 sec: 1.23x faster                                                      |
| xml_etree_process    | 43.4 ms                                                     | 37.6 ms: 1.16x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.04 us: 1.14x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 90.3 ms: 1.13x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.7 ms: 1.01x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 54.8 ms: 1.01x slower                                                       |
| unpickle_list        | 2.81 us                                                     | 2.90 us: 1.03x slower                                                       |
| pickle               | 6.80 us                                                     | 7.18 us: 1.05x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.3 us: 1.08x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.85 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.2 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.53 ms: 1.35x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230512-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a7+-f190abf |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.3 us: 3.41x faster                                                       |
| deltablue                | 4.17 ms                                                     | 2.07 ms: 2.02x faster                                                       |
| richards_super           | 51.7 ms                                                     | 28.6 ms: 1.81x faster                                                       |
| mypy2                    | 352 ms                                                      | 213 ms: 1.65x faster                                                        |
| logging_silent           | 96.4 ns                                                     | 58.6 ns: 1.65x faster                                                       |
| richards                 | 41.2 ms                                                     | 25.2 ms: 1.63x faster                                                       |
| go                       | 136 ms                                                      | 85.0 ms: 1.60x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 784 us: 1.55x faster                                                        |
| async_tree_memoization   | 497 ms                                                      | 329 ms: 1.51x faster                                                        |
| scimark_lu               | 85.4 ms                                                     | 56.5 ms: 1.51x faster                                                       |
| json_dumps               | 8.50 ms                                                     | 5.69 ms: 1.49x faster                                                       |
| async_tree_none          | 420 ms                                                      | 282 ms: 1.49x faster                                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 983 us: 1.49x faster                                                        |
| async_tree_io            | 1.07 sec                                                    | 719 ms: 1.48x faster                                                        |
| asyncio_tcp              | 712 ms                                                      | 483 ms: 1.47x faster                                                        |
| raytrace                 | 271 ms                                                      | 184 ms: 1.47x faster                                                        |
| generators               | 31.6 ms                                                     | 21.5 ms: 1.47x faster                                                       |
| hexiom                   | 5.52 ms                                                     | 3.86 ms: 1.43x faster                                                       |
| pickle_pure_python       | 257 us                                                      | 187 us: 1.37x faster                                                        |
| chaos                    | 58.9 ms                                                     | 43.1 ms: 1.37x faster                                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 41.3 ms: 1.35x faster                                                       |
| pyflate                  | 387 ms                                                      | 286 ms: 1.35x faster                                                        |
| scimark_sor              | 105 ms                                                      | 77.6 ms: 1.35x faster                                                       |
| mako                     | 8.80 ms                                                     | 6.53 ms: 1.35x faster                                                       |
| crypto_pyaes             | 62.3 ms                                                     | 47.3 ms: 1.32x faster                                                       |
| unpickle_pure_python     | 171 us                                                      | 130 us: 1.32x faster                                                        |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 470 ms: 1.30x faster                                                        |
| pycparser                | 868 ms                                                      | 675 ms: 1.29x faster                                                        |
| spectral_norm            | 78.0 ms                                                     | 62.1 ms: 1.26x faster                                                       |
| deepcopy_memo            | 28.5 us                                                     | 22.8 us: 1.25x faster                                                       |
| tomli_loads              | 1.62 sec                                                    | 1.32 sec: 1.23x faster                                                      |
| regex_compile            | 103 ms                                                      | 84.2 ms: 1.23x faster                                                       |
| tornado_http             | 109 ms                                                      | 89.5 ms: 1.22x faster                                                       |
| mdp                      | 1.71 sec                                                    | 1.42 sec: 1.21x faster                                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.03 sec: 1.18x faster                                                      |
| docutils                 | 1.89 sec                                                    | 1.61 sec: 1.18x faster                                                      |
| pprint_safe_repr         | 589 ms                                                      | 501 ms: 1.17x faster                                                        |
| float                    | 60.2 ms                                                     | 51.6 ms: 1.17x faster                                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 33.6 ms: 1.16x faster                                                       |
| xml_etree_process        | 43.4 ms                                                     | 37.6 ms: 1.16x faster                                                       |
| 2to3                     | 237 ms                                                      | 206 ms: 1.15x faster                                                        |
| bench_thread_pool        | 946 us                                                      | 826 us: 1.15x faster                                                        |
| unpickle                 | 9.17 us                                                     | 8.04 us: 1.14x faster                                                       |
| coroutines               | 15.9 ms                                                     | 14.0 ms: 1.14x faster                                                       |
| scimark_fft              | 193 ms                                                      | 170 ms: 1.14x faster                                                        |
| comprehensions           | 16.0 us                                                     | 14.1 us: 1.13x faster                                                       |
| aiohttp                  | 1.01 ms                                                     | 889 us: 1.13x faster                                                        |
| xml_etree_parse          | 102 ms                                                      | 90.3 ms: 1.13x faster                                                       |
| nqueens                  | 67.0 ms                                                     | 60.1 ms: 1.12x faster                                                       |
| dulwich_log              | 47.6 ms                                                     | 42.7 ms: 1.12x faster                                                       |
| deepcopy                 | 255 us                                                      | 229 us: 1.11x faster                                                        |
| create_gc_cycles         | 782 us                                                      | 702 us: 1.11x faster                                                        |
| sqlglot_normalize        | 202 ms                                                      | 182 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.41 ms: 1.10x faster                                                       |
| regex_dna                | 132 ms                                                      | 120 ms: 1.10x faster                                                        |
| fannkuch                 | 258 ms                                                      | 235 ms: 1.10x faster                                                        |
| sqlite_synth             | 1.84 us                                                     | 1.71 us: 1.07x faster                                                       |
| regex_v8                 | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.02 us: 1.07x faster                                                       |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.94 sec: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                       |
| python_startup           | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                                       |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.04x faster                                                       |
| json                     | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                                       |
| nbody                    | 69.3 ms                                                     | 68.3 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 63.5 ms                                                     | 62.7 ms: 1.01x faster                                                       |
| meteor_contest           | 72.5 ms                                                     | 72.3 ms: 1.00x faster                                                       |
| xml_etree_generate       | 54.5 ms                                                     | 54.8 ms: 1.01x slower                                                       |
| unpickle_list            | 2.81 us                                                     | 2.90 us: 1.03x slower                                                       |
| pidigits                 | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| logging_simple           | 6.20 us                                                     | 6.44 us: 1.04x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.2 ms: 1.04x slower                                                       |
| async_generators         | 224 ms                                                      | 234 ms: 1.05x slower                                                        |
| logging_format           | 6.66 us                                                     | 7.00 us: 1.05x slower                                                       |
| pickle                   | 6.80 us                                                     | 7.18 us: 1.05x slower                                                       |
| pathlib                  | 77.4 ms                                                     | 81.8 ms: 1.06x slower                                                       |
| pickle_dict              | 16.9 us                                                     | 18.3 us: 1.08x slower                                                       |
| telco                    | 3.78 ms                                                     | 4.08 ms: 1.08x slower                                                       |
| gc_traversal             | 1.34 ms                                                     | 1.47 ms: 1.10x slower                                                       |
| pickle_list              | 2.59 us                                                     | 2.85 us: 1.10x slower                                                       |
| bench_mp_pool            | 60.7 ms                                                     | 67.0 ms: 1.10x slower                                                       |
| dask                     | 305 ms                                                      | 361 ms: 1.19x slower                                                        |
| coverage                 | 40.0 ms                                                     | 52.0 ms: 1.30x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): unpack_sequence
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
