
# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_calls_to_
- machine: linux-x86_64
- commit hash: 1df353e
- commit date: 2023-06-18
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                                                |
| tornado_http   | 152 ms                                                       | 121 ms: 1.26x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 86.9 ms: 1.58x faster                                                                 |
| float          | 110 ms                                                       | 78.6 ms: 1.40x faster                                                                 |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 143 ms: 1.35x faster                                                                  |
| regex_v8       | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                                                 |
| regex_dna      | 259 ms                                                       | 250 ms: 1.04x faster                                                                  |
| regex_effbot   | 2.99 ms                                                      | 3.63 ms: 1.21x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 214 us: 1.50x faster                                                                  |
| pickle_pure_python   | 457 us                                                       | 322 us: 1.42x faster                                                                  |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                                 |
| tomli_loads          | 2.97 sec                                                     | 2.21 sec: 1.34x faster                                                                |
| xml_etree_process    | 76.0 ms                                                      | 58.5 ms: 1.30x faster                                                                 |
| json_loads           | 30.0 us                                                      | 24.9 us: 1.20x faster                                                                 |
| xml_etree_generate   | 94.6 ms                                                      | 85.5 ms: 1.11x faster                                                                 |
| xml_etree_parse      | 162 ms                                                       | 151 ms: 1.07x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                                  |
| pickle               | 9.94 us                                                      | 10.0 us: 1.01x slower                                                                 |
| unpickle             | 14.2 us                                                      | 14.5 us: 1.02x slower                                                                 |
| unpickle_list        | 4.49 us                                                      | 4.68 us: 1.04x slower                                                                 |
| pickle_dict          | 30.0 us                                                      | 32.0 us: 1.07x slower                                                                 |
| pickle_list          | 4.11 us                                                      | 4.46 us: 1.09x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                                 |
| python_startup_no_site | 7.32 ms                                                      | 8.36 ms: 1.14x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf2-x86_64-faster%2dcpython-specialize_calls_to_-3.13.0a0-1df353e |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 150 us: 3.47x faster                                                                  |
| deltablue                | 7.47 ms                                                      | 3.22 ms: 2.32x faster                                                                 |
| asyncio_tcp              | 782 ms                                                       | 378 ms: 2.07x faster                                                                  |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.56 sec: 1.98x faster                                                                |
| logging_silent           | 166 ns                                                       | 92.7 ns: 1.79x faster                                                                 |
| chaos                    | 107 ms                                                       | 60.3 ms: 1.78x faster                                                                 |
| raytrace                 | 488 ms                                                       | 278 ms: 1.76x faster                                                                  |
| go                       | 259 ms                                                       | 148 ms: 1.75x faster                                                                  |
| scimark_lu               | 164 ms                                                       | 93.8 ms: 1.75x faster                                                                 |
| richards_super           | 90.8 ms                                                      | 53.5 ms: 1.70x faster                                                                 |
| scimark_sor              | 177 ms                                                       | 108 ms: 1.64x faster                                                                  |
| hexiom                   | 9.52 ms                                                      | 5.81 ms: 1.64x faster                                                                 |
| richards                 | 74.1 ms                                                      | 46.4 ms: 1.60x faster                                                                 |
| sqlglot_parse            | 2.26 ms                                                      | 1.42 ms: 1.59x faster                                                                 |
| nbody                    | 137 ms                                                       | 86.9 ms: 1.58x faster                                                                 |
| generators               | 58.0 ms                                                      | 37.0 ms: 1.57x faster                                                                 |
| pyflate                  | 697 ms                                                       | 446 ms: 1.56x faster                                                                  |
| spectral_norm            | 136 ms                                                       | 88.0 ms: 1.55x faster                                                                 |
| scimark_monte_carlo      | 109 ms                                                       | 70.8 ms: 1.55x faster                                                                 |
| async_tree_none          | 700 ms                                                       | 463 ms: 1.51x faster                                                                  |
| async_tree_io            | 1.61 sec                                                     | 1.06 sec: 1.51x faster                                                                |
| unpickle_pure_python     | 321 us                                                       | 214 us: 1.50x faster                                                                  |
| sqlglot_transpile        | 2.71 ms                                                      | 1.82 ms: 1.49x faster                                                                 |
| async_tree_memoization   | 824 ms                                                       | 557 ms: 1.48x faster                                                                  |
| mako                     | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                                                 |
| crypto_pyaes             | 118 ms                                                       | 81.3 ms: 1.45x faster                                                                 |
| pickle_pure_python       | 457 us                                                       | 322 us: 1.42x faster                                                                  |
| float                    | 110 ms                                                       | 78.6 ms: 1.40x faster                                                                 |
| coroutines               | 30.4 ms                                                      | 22.1 ms: 1.38x faster                                                                 |
| fannkuch                 | 496 ms                                                       | 361 ms: 1.37x faster                                                                  |
| json_dumps               | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                                 |
| regex_compile            | 194 ms                                                       | 143 ms: 1.35x faster                                                                  |
| tomli_loads              | 2.97 sec                                                     | 2.21 sec: 1.34x faster                                                                |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 710 ms: 1.34x faster                                                                  |
| logging_simple           | 8.90 us                                                      | 6.82 us: 1.31x faster                                                                 |
| xml_etree_process        | 76.0 ms                                                      | 58.5 ms: 1.30x faster                                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 815 ms: 1.29x faster                                                                  |
| logging_format           | 9.57 us                                                      | 7.43 us: 1.29x faster                                                                 |
| pycparser                | 1.66 sec                                                     | 1.29 sec: 1.28x faster                                                                |
| deepcopy_memo            | 48.9 us                                                      | 38.3 us: 1.28x faster                                                                 |
| mypy2                    | 466 ms                                                       | 370 ms: 1.26x faster                                                                  |
| tornado_http             | 152 ms                                                       | 121 ms: 1.26x faster                                                                  |
| nqueens                  | 112 ms                                                       | 90.4 ms: 1.24x faster                                                                 |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.23x faster                                                                  |
| comprehensions           | 26.9 us                                                      | 22.0 us: 1.22x faster                                                                 |
| dulwich_log              | 80.1 ms                                                      | 65.6 ms: 1.22x faster                                                                 |
| sqlglot_optimize         | 70.3 ms                                                      | 58.0 ms: 1.21x faster                                                                 |
| deepcopy                 | 454 us                                                       | 376 us: 1.21x faster                                                                  |
| mdp                      | 3.03 sec                                                     | 2.52 sec: 1.20x faster                                                                |
| json_loads               | 30.0 us                                                      | 24.9 us: 1.20x faster                                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 947 us: 1.20x faster                                                                  |
| scimark_fft              | 359 ms                                                       | 305 ms: 1.18x faster                                                                  |
| docutils                 | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                                                |
| json                     | 5.96 ms                                                      | 5.11 ms: 1.17x faster                                                                 |
| unpack_sequence          | 59.5 ns                                                      | 51.2 ns: 1.16x faster                                                                 |
| deepcopy_reduce          | 4.03 us                                                      | 3.47 us: 1.16x faster                                                                 |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.47 ms: 1.16x faster                                                                 |
| create_gc_cycles         | 1.82 ms                                                      | 1.61 ms: 1.13x faster                                                                 |
| regex_v8                 | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                                                 |
| xml_etree_generate       | 94.6 ms                                                      | 85.5 ms: 1.11x faster                                                                 |
| meteor_contest           | 137 ms                                                       | 125 ms: 1.09x faster                                                                  |
| pathlib                  | 21.7 ms                                                      | 19.9 ms: 1.09x faster                                                                 |
| sqlite_synth             | 2.97 us                                                      | 2.73 us: 1.09x faster                                                                 |
| xml_etree_parse          | 162 ms                                                       | 151 ms: 1.07x faster                                                                  |
| async_generators         | 422 ms                                                       | 397 ms: 1.06x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                                                  |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                                                  |
| regex_dna                | 259 ms                                                       | 250 ms: 1.04x faster                                                                  |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                                 |
| pickle                   | 9.94 us                                                      | 10.0 us: 1.01x slower                                                                 |
| telco                    | 7.14 ms                                                      | 7.23 ms: 1.01x slower                                                                 |
| unpickle                 | 14.2 us                                                      | 14.5 us: 1.02x slower                                                                 |
| gc_traversal             | 3.45 ms                                                      | 3.57 ms: 1.03x slower                                                                 |
| unpickle_list            | 4.49 us                                                      | 4.68 us: 1.04x slower                                                                 |
| pickle_dict              | 30.0 us                                                      | 32.0 us: 1.07x slower                                                                 |
| pickle_list              | 4.11 us                                                      | 4.46 us: 1.09x slower                                                                 |
| python_startup_no_site   | 7.32 ms                                                      | 8.36 ms: 1.14x slower                                                                 |
| regex_effbot             | 2.99 ms                                                      | 3.63 ms: 1.21x slower                                                                 |
| coverage                 | 64.0 ms                                                      | 85.3 ms: 1.33x slower                                                                 |
| bench_mp_pool            | 7.18 ms                                                      | 16.1 ms: 2.24x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                                          |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x
