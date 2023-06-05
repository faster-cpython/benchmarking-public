
# Results vs. 3.10.4

- fork: faster-cpython
- ref: remove_remaining_sup
- machine: linux-x86_64
- commit hash: 6cde1a4
- commit date: 2023-06-02
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                                                |
| tornado_http   | 152 ms                                                       | 117 ms: 1.30x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 87.9 ms: 1.56x faster                                                                 |
| float          | 110 ms                                                       | 78.4 ms: 1.41x faster                                                                 |
| pidigits       | 271 ms                                                       | 261 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 147 ms: 1.31x faster                                                                  |
| regex_v8       | 26.6 ms                                                      | 24.4 ms: 1.09x faster                                                                 |
| regex_dna      | 259 ms                                                       | 245 ms: 1.06x faster                                                                  |
| regex_effbot   | 2.99 ms                                                      | 3.62 ms: 1.21x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 212 us: 1.51x faster                                                                  |
| pickle_pure_python   | 457 us                                                       | 322 us: 1.42x faster                                                                  |
| json_dumps           | 14.2 ms                                                      | 10.1 ms: 1.40x faster                                                                 |
| tomli_loads          | 2.97 sec                                                     | 2.22 sec: 1.34x faster                                                                |
| xml_etree_process    | 76.0 ms                                                      | 59.9 ms: 1.27x faster                                                                 |
| json_loads           | 30.0 us                                                      | 24.5 us: 1.22x faster                                                                 |
| xml_etree_parse      | 162 ms                                                       | 148 ms: 1.09x faster                                                                  |
| xml_etree_generate   | 94.6 ms                                                      | 87.4 ms: 1.08x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                                                  |
| pickle               | 9.94 us                                                      | 10.0 us: 1.01x slower                                                                 |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                                                 |
| unpickle_list        | 4.49 us                                                      | 4.64 us: 1.03x slower                                                                 |
| pickle_list          | 4.11 us                                                      | 4.27 us: 1.04x slower                                                                 |
| pickle_dict          | 30.0 us                                                      | 31.8 us: 1.06x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                                                 |
| python_startup_no_site | 7.32 ms                                                      | 8.33 ms: 1.14x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 150 us: 3.49x faster                                                                  |
| deltablue                | 7.47 ms                                                      | 3.24 ms: 2.30x faster                                                                 |
| asyncio_tcp              | 782 ms                                                       | 382 ms: 2.05x faster                                                                  |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                                                |
| scimark_lu               | 164 ms                                                       | 94.8 ms: 1.73x faster                                                                 |
| logging_silent           | 166 ns                                                       | 96.7 ns: 1.71x faster                                                                 |
| richards_super           | 90.8 ms                                                      | 53.3 ms: 1.70x faster                                                                 |
| go                       | 259 ms                                                       | 153 ms: 1.69x faster                                                                  |
| chaos                    | 107 ms                                                       | 63.6 ms: 1.69x faster                                                                 |
| generators               | 58.0 ms                                                      | 35.8 ms: 1.62x faster                                                                 |
| scimark_sor              | 177 ms                                                       | 109 ms: 1.62x faster                                                                  |
| sqlglot_parse            | 2.26 ms                                                      | 1.41 ms: 1.61x faster                                                                 |
| hexiom                   | 9.52 ms                                                      | 5.95 ms: 1.60x faster                                                                 |
| scimark_monte_carlo      | 109 ms                                                       | 68.8 ms: 1.59x faster                                                                 |
| raytrace                 | 488 ms                                                       | 308 ms: 1.59x faster                                                                  |
| richards                 | 74.1 ms                                                      | 47.4 ms: 1.56x faster                                                                 |
| nbody                    | 137 ms                                                       | 87.9 ms: 1.56x faster                                                                 |
| spectral_norm            | 136 ms                                                       | 88.0 ms: 1.55x faster                                                                 |
| pyflate                  | 697 ms                                                       | 451 ms: 1.55x faster                                                                  |
| unpickle_pure_python     | 321 us                                                       | 212 us: 1.51x faster                                                                  |
| async_tree_io            | 1.61 sec                                                     | 1.07 sec: 1.51x faster                                                                |
| sqlglot_transpile        | 2.71 ms                                                      | 1.80 ms: 1.51x faster                                                                 |
| async_tree_none          | 700 ms                                                       | 466 ms: 1.50x faster                                                                  |
| async_tree_memoization   | 824 ms                                                       | 558 ms: 1.48x faster                                                                  |
| crypto_pyaes             | 118 ms                                                       | 81.1 ms: 1.46x faster                                                                 |
| mako                     | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                                 |
| pickle_pure_python       | 457 us                                                       | 322 us: 1.42x faster                                                                  |
| float                    | 110 ms                                                       | 78.4 ms: 1.41x faster                                                                 |
| json_dumps               | 14.2 ms                                                      | 10.1 ms: 1.40x faster                                                                 |
| fannkuch                 | 496 ms                                                       | 358 ms: 1.39x faster                                                                  |
| coroutines               | 30.4 ms                                                      | 22.1 ms: 1.37x faster                                                                 |
| tomli_loads              | 2.97 sec                                                     | 2.22 sec: 1.34x faster                                                                |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 711 ms: 1.34x faster                                                                  |
| regex_compile            | 194 ms                                                       | 147 ms: 1.31x faster                                                                  |
| logging_simple           | 8.90 us                                                      | 6.83 us: 1.30x faster                                                                 |
| logging_format           | 9.57 us                                                      | 7.37 us: 1.30x faster                                                                 |
| tornado_http             | 152 ms                                                       | 117 ms: 1.30x faster                                                                  |
| pycparser                | 1.66 sec                                                     | 1.28 sec: 1.30x faster                                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                                                |
| mypy2                    | 466 ms                                                       | 365 ms: 1.28x faster                                                                  |
| deepcopy_memo            | 48.9 us                                                      | 38.4 us: 1.27x faster                                                                 |
| xml_etree_process        | 76.0 ms                                                      | 59.9 ms: 1.27x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 827 ms: 1.27x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                                                  |
| unpack_sequence          | 59.5 ns                                                      | 48.3 ns: 1.23x faster                                                                 |
| nqueens                  | 112 ms                                                       | 91.4 ms: 1.23x faster                                                                 |
| comprehensions           | 26.9 us                                                      | 21.9 us: 1.23x faster                                                                 |
| json_loads               | 30.0 us                                                      | 24.5 us: 1.22x faster                                                                 |
| dulwich_log              | 80.1 ms                                                      | 65.6 ms: 1.22x faster                                                                 |
| sqlglot_optimize         | 70.3 ms                                                      | 57.9 ms: 1.21x faster                                                                 |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.29 ms: 1.21x faster                                                                 |
| deepcopy                 | 454 us                                                       | 377 us: 1.20x faster                                                                  |
| mdp                      | 3.03 sec                                                     | 2.52 sec: 1.20x faster                                                                |
| scimark_fft              | 359 ms                                                       | 302 ms: 1.19x faster                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.18x faster                                                                  |
| docutils                 | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                                                |
| deepcopy_reduce          | 4.03 us                                                      | 3.43 us: 1.17x faster                                                                 |
| json                     | 5.96 ms                                                      | 5.13 ms: 1.16x faster                                                                 |
| create_gc_cycles         | 1.82 ms                                                      | 1.63 ms: 1.12x faster                                                                 |
| pathlib                  | 21.7 ms                                                      | 19.7 ms: 1.10x faster                                                                 |
| sqlite_synth             | 2.97 us                                                      | 2.70 us: 1.10x faster                                                                 |
| regex_v8                 | 26.6 ms                                                      | 24.4 ms: 1.09x faster                                                                 |
| xml_etree_parse          | 162 ms                                                       | 148 ms: 1.09x faster                                                                  |
| xml_etree_generate       | 94.6 ms                                                      | 87.4 ms: 1.08x faster                                                                 |
| async_generators         | 422 ms                                                       | 394 ms: 1.07x faster                                                                  |
| meteor_contest           | 137 ms                                                       | 129 ms: 1.06x faster                                                                  |
| regex_dna                | 259 ms                                                       | 245 ms: 1.06x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                                                  |
| pidigits                 | 271 ms                                                       | 261 ms: 1.03x faster                                                                  |
| python_startup           | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                                                 |
| pickle                   | 9.94 us                                                      | 10.0 us: 1.01x slower                                                                 |
| telco                    | 7.14 ms                                                      | 7.24 ms: 1.01x slower                                                                 |
| unpickle                 | 14.2 us                                                      | 14.6 us: 1.03x slower                                                                 |
| gc_traversal             | 3.45 ms                                                      | 3.56 ms: 1.03x slower                                                                 |
| unpickle_list            | 4.49 us                                                      | 4.64 us: 1.03x slower                                                                 |
| pickle_list              | 4.11 us                                                      | 4.27 us: 1.04x slower                                                                 |
| pickle_dict              | 30.0 us                                                      | 31.8 us: 1.06x slower                                                                 |
| python_startup_no_site   | 7.32 ms                                                      | 8.33 ms: 1.14x slower                                                                 |
| regex_effbot             | 2.99 ms                                                      | 3.62 ms: 1.21x slower                                                                 |
| bench_mp_pool            | 7.18 ms                                                      | 9.37 ms: 1.31x slower                                                                 |
| coverage                 | 64.0 ms                                                      | 89.1 ms: 1.39x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                                          |
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
