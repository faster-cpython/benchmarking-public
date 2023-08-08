
# Results vs. 3.10.4

- fork: faster-cpython
- ref: tweak_ints_monitorin
- machine: linux-x86_64
- commit hash: 83ffca9
- commit date: 2023-08-05
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                                                |
| tornado_http   | 152 ms                                                       | 122 ms: 1.25x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 88.9 ms: 1.54x faster                                                                 |
| float          | 110 ms                                                       | 81.3 ms: 1.36x faster                                                                 |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 151 ms: 1.28x faster                                                                  |
| regex_v8       | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                                                 |
| regex_dna      | 259 ms                                                       | 237 ms: 1.10x faster                                                                  |
| regex_effbot   | 2.99 ms                                                      | 3.47 ms: 1.16x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 223 us: 1.44x faster                                                                  |
| pickle_pure_python   | 457 us                                                       | 326 us: 1.40x faster                                                                  |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                                 |
| xml_etree_process    | 76.0 ms                                                      | 60.8 ms: 1.25x faster                                                                 |
| tomli_loads          | 2.97 sec                                                     | 2.42 sec: 1.23x faster                                                                |
| json_loads           | 30.0 us                                                      | 25.5 us: 1.17x faster                                                                 |
| xml_etree_generate   | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                                                 |
| xml_etree_parse      | 162 ms                                                       | 148 ms: 1.09x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                                                  |
| pickle               | 9.94 us                                                      | 9.99 us: 1.01x slower                                                                 |
| unpickle             | 14.2 us                                                      | 14.7 us: 1.03x slower                                                                 |
| pickle_list          | 4.11 us                                                      | 4.34 us: 1.06x slower                                                                 |
| pickle_dict          | 30.0 us                                                      | 31.9 us: 1.07x slower                                                                 |
| unpickle_list        | 4.49 us                                                      | 4.85 us: 1.08x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                                                 |
| python_startup_no_site | 7.32 ms                                                      | 8.64 ms: 1.18x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 155 us: 3.38x faster                                                                  |
| asyncio_tcp              | 782 ms                                                       | 368 ms: 2.13x faster                                                                  |
| deltablue                | 7.47 ms                                                      | 3.64 ms: 2.05x faster                                                                 |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                                                |
| raytrace                 | 488 ms                                                       | 280 ms: 1.74x faster                                                                  |
| chaos                    | 107 ms                                                       | 62.8 ms: 1.71x faster                                                                 |
| logging_silent           | 166 ns                                                       | 97.2 ns: 1.70x faster                                                                 |
| scimark_lu               | 164 ms                                                       | 100 ms: 1.63x faster                                                                  |
| crypto_pyaes             | 118 ms                                                       | 74.3 ms: 1.59x faster                                                                 |
| scimark_monte_carlo      | 109 ms                                                       | 69.0 ms: 1.59x faster                                                                 |
| sqlglot_parse            | 2.26 ms                                                      | 1.44 ms: 1.57x faster                                                                 |
| generators               | 58.0 ms                                                      | 37.4 ms: 1.55x faster                                                                 |
| nbody                    | 137 ms                                                       | 88.9 ms: 1.54x faster                                                                 |
| richards_super           | 90.8 ms                                                      | 60.8 ms: 1.49x faster                                                                 |
| async_tree_none          | 700 ms                                                       | 471 ms: 1.49x faster                                                                  |
| bench_mp_pool            | 7.18 ms                                                      | 4.84 ms: 1.48x faster                                                                 |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.48x faster                                                                |
| sqlglot_transpile        | 2.71 ms                                                      | 1.85 ms: 1.46x faster                                                                 |
| spectral_norm            | 136 ms                                                       | 93.4 ms: 1.46x faster                                                                 |
| async_tree_memoization   | 824 ms                                                       | 569 ms: 1.45x faster                                                                  |
| hexiom                   | 9.52 ms                                                      | 6.58 ms: 1.45x faster                                                                 |
| go                       | 259 ms                                                       | 179 ms: 1.44x faster                                                                  |
| unpickle_pure_python     | 321 us                                                       | 223 us: 1.44x faster                                                                  |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                                 |
| pickle_pure_python       | 457 us                                                       | 326 us: 1.40x faster                                                                  |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                                 |
| richards                 | 74.1 ms                                                      | 53.7 ms: 1.38x faster                                                                 |
| float                    | 110 ms                                                       | 81.3 ms: 1.36x faster                                                                 |
| pyflate                  | 697 ms                                                       | 514 ms: 1.36x faster                                                                  |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 717 ms: 1.33x faster                                                                  |
| coroutines               | 30.4 ms                                                      | 23.3 ms: 1.30x faster                                                                 |
| logging_simple           | 8.90 us                                                      | 6.85 us: 1.30x faster                                                                 |
| logging_format           | 9.57 us                                                      | 7.40 us: 1.29x faster                                                                 |
| regex_compile            | 194 ms                                                       | 151 ms: 1.28x faster                                                                  |
| deepcopy_memo            | 48.9 us                                                      | 38.2 us: 1.28x faster                                                                 |
| fannkuch                 | 496 ms                                                       | 389 ms: 1.27x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.27x faster                                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 826 ms: 1.27x faster                                                                  |
| mypy2                    | 466 ms                                                       | 372 ms: 1.25x faster                                                                  |
| xml_etree_process        | 76.0 ms                                                      | 60.8 ms: 1.25x faster                                                                 |
| tornado_http             | 152 ms                                                       | 122 ms: 1.25x faster                                                                  |
| nqueens                  | 112 ms                                                       | 91.3 ms: 1.23x faster                                                                 |
| tomli_loads              | 2.97 sec                                                     | 2.42 sec: 1.23x faster                                                                |
| pycparser                | 1.66 sec                                                     | 1.35 sec: 1.23x faster                                                                |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.23 ms: 1.23x faster                                                                 |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.23x faster                                                                  |
| scimark_sor              | 177 ms                                                       | 146 ms: 1.21x faster                                                                  |
| comprehensions           | 26.9 us                                                      | 22.3 us: 1.21x faster                                                                 |
| unpack_sequence          | 59.5 ns                                                      | 49.6 ns: 1.20x faster                                                                 |
| scimark_fft              | 359 ms                                                       | 301 ms: 1.19x faster                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 953 us: 1.19x faster                                                                  |
| sqlglot_optimize         | 70.3 ms                                                      | 59.4 ms: 1.18x faster                                                                 |
| deepcopy                 | 454 us                                                       | 384 us: 1.18x faster                                                                  |
| mdp                      | 3.03 sec                                                     | 2.57 sec: 1.18x faster                                                                |
| json_loads               | 30.0 us                                                      | 25.5 us: 1.17x faster                                                                 |
| dulwich_log              | 80.1 ms                                                      | 68.4 ms: 1.17x faster                                                                 |
| docutils                 | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                                                |
| deepcopy_reduce          | 4.03 us                                                      | 3.47 us: 1.16x faster                                                                 |
| json                     | 5.96 ms                                                      | 5.15 ms: 1.16x faster                                                                 |
| regex_v8                 | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                                                 |
| xml_etree_generate       | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                                                 |
| create_gc_cycles         | 1.82 ms                                                      | 1.66 ms: 1.10x faster                                                                 |
| pathlib                  | 21.7 ms                                                      | 19.8 ms: 1.10x faster                                                                 |
| regex_dna                | 259 ms                                                       | 237 ms: 1.10x faster                                                                  |
| sqlite_synth             | 2.97 us                                                      | 2.71 us: 1.09x faster                                                                 |
| xml_etree_parse          | 162 ms                                                       | 148 ms: 1.09x faster                                                                  |
| async_generators         | 422 ms                                                       | 397 ms: 1.06x faster                                                                  |
| meteor_contest           | 137 ms                                                       | 129 ms: 1.06x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                                                  |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                                                  |
| pickle                   | 9.94 us                                                      | 9.99 us: 1.01x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                                                 |
| gc_traversal             | 3.45 ms                                                      | 3.56 ms: 1.03x slower                                                                 |
| unpickle                 | 14.2 us                                                      | 14.7 us: 1.03x slower                                                                 |
| pickle_list              | 4.11 us                                                      | 4.34 us: 1.06x slower                                                                 |
| pickle_dict              | 30.0 us                                                      | 31.9 us: 1.07x slower                                                                 |
| unpickle_list            | 4.49 us                                                      | 4.85 us: 1.08x slower                                                                 |
| telco                    | 7.14 ms                                                      | 8.05 ms: 1.13x slower                                                                 |
| regex_effbot             | 2.99 ms                                                      | 3.47 ms: 1.16x slower                                                                 |
| python_startup_no_site   | 7.32 ms                                                      | 8.64 ms: 1.18x slower                                                                 |
| dask                     | 463 ms                                                       | 591 ms: 1.28x slower                                                                  |
| coverage                 | 64.0 ms                                                      | 83.9 ms: 1.31x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                          |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
