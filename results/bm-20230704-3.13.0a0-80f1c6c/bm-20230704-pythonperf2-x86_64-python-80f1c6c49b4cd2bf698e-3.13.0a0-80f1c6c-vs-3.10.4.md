
# Results vs. 3.10.4

- fork: python
- ref: 80f1c6c49b4cd2bf698e
- machine: linux-x86_64
- commit hash: 80f1c6c
- commit date: 2023-07-04
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.92 sec: 1.16x faster                                                      |
| tornado_http   | 152 ms                                                       | 123 ms: 1.23x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 85.6 ms: 1.60x faster                                                       |
| float          | 110 ms                                                       | 81.9 ms: 1.35x faster                                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 151 ms: 1.28x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 23.2 ms: 1.15x faster                                                       |
| regex_dna      | 259 ms                                                       | 237 ms: 1.09x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.38 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 219 us: 1.46x faster                                                        |
| pickle_pure_python   | 457 us                                                       | 330 us: 1.39x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                       |
| tomli_loads          | 2.97 sec                                                     | 2.32 sec: 1.28x faster                                                      |
| xml_etree_process    | 76.0 ms                                                      | 59.7 ms: 1.27x faster                                                       |
| json_loads           | 30.0 us                                                      | 24.5 us: 1.22x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 148 ms: 1.09x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 86.9 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.04x faster                                                        |
| unpickle             | 14.2 us                                                      | 14.4 us: 1.02x slower                                                       |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 31.2 us: 1.04x slower                                                       |
| unpickle_list        | 4.49 us                                                      | 4.71 us: 1.05x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.33 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.37 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-python-80f1c6c49b4cd2bf698e-3.13.0a0-80f1c6c |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 149 us: 3.51x faster                                                        |
| deltablue                | 7.47 ms                                                      | 3.55 ms: 2.10x faster                                                       |
| asyncio_tcp              | 782 ms                                                       | 382 ms: 2.05x faster                                                        |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                                      |
| raytrace                 | 488 ms                                                       | 278 ms: 1.76x faster                                                        |
| chaos                    | 107 ms                                                       | 61.6 ms: 1.74x faster                                                       |
| logging_silent           | 166 ns                                                       | 96.0 ns: 1.73x faster                                                       |
| scimark_lu               | 164 ms                                                       | 102 ms: 1.60x faster                                                        |
| nbody                    | 137 ms                                                       | 85.6 ms: 1.60x faster                                                       |
| generators               | 58.0 ms                                                      | 36.4 ms: 1.59x faster                                                       |
| richards_super           | 90.8 ms                                                      | 58.5 ms: 1.55x faster                                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.48 ms: 1.52x faster                                                       |
| async_tree_none          | 700 ms                                                       | 465 ms: 1.50x faster                                                        |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.49x faster                                                      |
| scimark_monte_carlo      | 109 ms                                                       | 74.0 ms: 1.48x faster                                                       |
| go                       | 259 ms                                                       | 176 ms: 1.47x faster                                                        |
| async_tree_memoization   | 824 ms                                                       | 560 ms: 1.47x faster                                                        |
| unpickle_pure_python     | 321 us                                                       | 219 us: 1.46x faster                                                        |
| hexiom                   | 9.52 ms                                                      | 6.57 ms: 1.45x faster                                                       |
| spectral_norm            | 136 ms                                                       | 94.4 ms: 1.44x faster                                                       |
| crypto_pyaes             | 118 ms                                                       | 82.6 ms: 1.43x faster                                                       |
| sqlglot_transpile        | 2.71 ms                                                      | 1.90 ms: 1.43x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| richards                 | 74.1 ms                                                      | 52.6 ms: 1.41x faster                                                       |
| pickle_pure_python       | 457 us                                                       | 330 us: 1.39x faster                                                        |
| json_dumps               | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                       |
| bench_mp_pool            | 7.18 ms                                                      | 5.29 ms: 1.36x faster                                                       |
| float                    | 110 ms                                                       | 81.9 ms: 1.35x faster                                                       |
| pyflate                  | 697 ms                                                       | 520 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 717 ms: 1.33x faster                                                        |
| coroutines               | 30.4 ms                                                      | 22.9 ms: 1.33x faster                                                       |
| logging_simple           | 8.90 us                                                      | 6.92 us: 1.28x faster                                                       |
| regex_compile            | 194 ms                                                       | 151 ms: 1.28x faster                                                        |
| tomli_loads              | 2.97 sec                                                     | 2.32 sec: 1.28x faster                                                      |
| logging_format           | 9.57 us                                                      | 7.51 us: 1.27x faster                                                       |
| xml_etree_process        | 76.0 ms                                                      | 59.7 ms: 1.27x faster                                                       |
| deepcopy_memo            | 48.9 us                                                      | 38.4 us: 1.27x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.27x faster                                                      |
| mypy2                    | 466 ms                                                       | 370 ms: 1.26x faster                                                        |
| fannkuch                 | 496 ms                                                       | 394 ms: 1.26x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 836 ms: 1.26x faster                                                        |
| pycparser                | 1.66 sec                                                     | 1.33 sec: 1.25x faster                                                      |
| nqueens                  | 112 ms                                                       | 91.2 ms: 1.23x faster                                                       |
| tornado_http             | 152 ms                                                       | 123 ms: 1.23x faster                                                        |
| json_loads               | 30.0 us                                                      | 24.5 us: 1.22x faster                                                       |
| comprehensions           | 26.9 us                                                      | 22.2 us: 1.21x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                        |
| scimark_sor              | 177 ms                                                       | 147 ms: 1.21x faster                                                        |
| mdp                      | 3.03 sec                                                     | 2.55 sec: 1.19x faster                                                      |
| deepcopy                 | 454 us                                                       | 382 us: 1.19x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 960 us: 1.18x faster                                                        |
| sqlglot_optimize         | 70.3 ms                                                      | 59.5 ms: 1.18x faster                                                       |
| dulwich_log              | 80.1 ms                                                      | 68.0 ms: 1.18x faster                                                       |
| docutils                 | 3.40 sec                                                     | 2.92 sec: 1.16x faster                                                      |
| json                     | 5.96 ms                                                      | 5.13 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.47 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.47 us: 1.16x faster                                                       |
| regex_v8                 | 26.6 ms                                                      | 23.2 ms: 1.15x faster                                                       |
| scimark_fft              | 359 ms                                                       | 313 ms: 1.15x faster                                                        |
| pathlib                  | 21.7 ms                                                      | 19.5 ms: 1.11x faster                                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.66 ms: 1.10x faster                                                       |
| regex_dna                | 259 ms                                                       | 237 ms: 1.09x faster                                                        |
| xml_etree_parse          | 162 ms                                                       | 148 ms: 1.09x faster                                                        |
| xml_etree_generate       | 94.6 ms                                                      | 86.9 ms: 1.09x faster                                                       |
| sqlite_synth             | 2.97 us                                                      | 2.74 us: 1.08x faster                                                       |
| meteor_contest           | 137 ms                                                       | 129 ms: 1.06x faster                                                        |
| async_generators         | 422 ms                                                       | 400 ms: 1.05x faster                                                        |
| unpack_sequence          | 59.5 ns                                                      | 56.7 ns: 1.05x faster                                                       |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.04x faster                                                        |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                       |
| unpickle                 | 14.2 us                                                      | 14.4 us: 1.02x slower                                                       |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.03x slower                                                       |
| pickle_dict              | 30.0 us                                                      | 31.2 us: 1.04x slower                                                       |
| gc_traversal             | 3.45 ms                                                      | 3.59 ms: 1.04x slower                                                       |
| unpickle_list            | 4.49 us                                                      | 4.71 us: 1.05x slower                                                       |
| pickle_list              | 4.11 us                                                      | 4.33 us: 1.05x slower                                                       |
| telco                    | 7.14 ms                                                      | 7.79 ms: 1.09x slower                                                       |
| regex_effbot             | 2.99 ms                                                      | 3.38 ms: 1.13x slower                                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.37 ms: 1.14x slower                                                       |
| dask                     | 463 ms                                                       | 593 ms: 1.28x slower                                                        |
| coverage                 | 64.0 ms                                                      | 87.5 ms: 1.37x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
