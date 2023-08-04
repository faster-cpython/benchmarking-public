
# Results vs. 3.10.4

- fork: python
- ref: 2ba7c7f7b151ff56cf12
- machine: linux-x86_64
- commit hash: 2ba7c7f
- commit date: 2023-08-04
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| tornado_http   | 152 ms                                                       | 121 ms: 1.25x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.2 ms: 1.54x faster                                                       |
| float          | 110 ms                                                       | 80.7 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 149 ms: 1.30x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                                       |
| regex_dna      | 259 ms                                                       | 242 ms: 1.07x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.77 ms: 1.26x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 323 us: 1.42x faster                                                        |
| unpickle_pure_python | 321 us                                                       | 233 us: 1.38x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                       |
| tomli_loads          | 2.97 sec                                                     | 2.29 sec: 1.30x faster                                                      |
| xml_etree_process    | 76.0 ms                                                      | 59.1 ms: 1.29x faster                                                       |
| json_loads           | 30.0 us                                                      | 24.5 us: 1.22x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 86.5 ms: 1.09x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 152 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.03x faster                                                        |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                                       |
| unpickle             | 14.2 us                                                      | 14.7 us: 1.04x slower                                                       |
| unpickle_list        | 4.49 us                                                      | 4.69 us: 1.04x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 32.6 us: 1.09x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.54 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.63 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.45x faster                                                        |
| asyncio_tcp              | 782 ms                                                       | 373 ms: 2.10x faster                                                        |
| deltablue                | 7.47 ms                                                      | 3.70 ms: 2.02x faster                                                       |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| raytrace                 | 488 ms                                                       | 275 ms: 1.77x faster                                                        |
| chaos                    | 107 ms                                                       | 62.5 ms: 1.71x faster                                                       |
| scimark_lu               | 164 ms                                                       | 97.9 ms: 1.67x faster                                                       |
| logging_silent           | 166 ns                                                       | 101 ns: 1.64x faster                                                        |
| crypto_pyaes             | 118 ms                                                       | 73.6 ms: 1.61x faster                                                       |
| scimark_monte_carlo      | 109 ms                                                       | 68.2 ms: 1.61x faster                                                       |
| generators               | 58.0 ms                                                      | 36.7 ms: 1.58x faster                                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.44 ms: 1.57x faster                                                       |
| nbody                    | 137 ms                                                       | 89.2 ms: 1.54x faster                                                       |
| bench_mp_pool            | 7.18 ms                                                      | 4.72 ms: 1.52x faster                                                       |
| async_tree_io            | 1.61 sec                                                     | 1.09 sec: 1.48x faster                                                      |
| async_tree_none          | 700 ms                                                       | 474 ms: 1.48x faster                                                        |
| sqlglot_transpile        | 2.71 ms                                                      | 1.84 ms: 1.47x faster                                                       |
| richards_super           | 90.8 ms                                                      | 61.7 ms: 1.47x faster                                                       |
| hexiom                   | 9.52 ms                                                      | 6.48 ms: 1.47x faster                                                       |
| go                       | 259 ms                                                       | 176 ms: 1.47x faster                                                        |
| async_tree_memoization   | 824 ms                                                       | 569 ms: 1.45x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |
| pickle_pure_python       | 457 us                                                       | 323 us: 1.42x faster                                                        |
| spectral_norm            | 136 ms                                                       | 97.6 ms: 1.40x faster                                                       |
| unpickle_pure_python     | 321 us                                                       | 233 us: 1.38x faster                                                        |
| json_dumps               | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                       |
| float                    | 110 ms                                                       | 80.7 ms: 1.37x faster                                                       |
| pyflate                  | 697 ms                                                       | 515 ms: 1.35x faster                                                        |
| richards                 | 74.1 ms                                                      | 55.2 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 719 ms: 1.32x faster                                                        |
| coroutines               | 30.4 ms                                                      | 23.3 ms: 1.30x faster                                                       |
| regex_compile            | 194 ms                                                       | 149 ms: 1.30x faster                                                        |
| tomli_loads              | 2.97 sec                                                     | 2.29 sec: 1.30x faster                                                      |
| logging_simple           | 8.90 us                                                      | 6.87 us: 1.29x faster                                                       |
| deepcopy_memo            | 48.9 us                                                      | 37.9 us: 1.29x faster                                                       |
| xml_etree_process        | 76.0 ms                                                      | 59.1 ms: 1.29x faster                                                       |
| logging_format           | 9.57 us                                                      | 7.45 us: 1.28x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.28x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 824 ms: 1.27x faster                                                        |
| fannkuch                 | 496 ms                                                       | 395 ms: 1.26x faster                                                        |
| tornado_http             | 152 ms                                                       | 121 ms: 1.25x faster                                                        |
| pycparser                | 1.66 sec                                                     | 1.33 sec: 1.25x faster                                                      |
| mypy2                    | 466 ms                                                       | 372 ms: 1.25x faster                                                        |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.21 ms: 1.23x faster                                                       |
| nqueens                  | 112 ms                                                       | 91.2 ms: 1.23x faster                                                       |
| scimark_sor              | 177 ms                                                       | 144 ms: 1.23x faster                                                        |
| json_loads               | 30.0 us                                                      | 24.5 us: 1.22x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                        |
| comprehensions           | 26.9 us                                                      | 22.2 us: 1.21x faster                                                       |
| unpack_sequence          | 59.5 ns                                                      | 49.6 ns: 1.20x faster                                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 59.0 ms: 1.19x faster                                                       |
| scimark_fft              | 359 ms                                                       | 304 ms: 1.18x faster                                                        |
| mdp                      | 3.03 sec                                                     | 2.58 sec: 1.18x faster                                                      |
| bench_thread_pool        | 1.14 ms                                                      | 966 us: 1.18x faster                                                        |
| deepcopy                 | 454 us                                                       | 387 us: 1.17x faster                                                        |
| deepcopy_reduce          | 4.03 us                                                      | 3.45 us: 1.17x faster                                                       |
| docutils                 | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| json                     | 5.96 ms                                                      | 5.12 ms: 1.17x faster                                                       |
| dulwich_log              | 80.1 ms                                                      | 69.1 ms: 1.16x faster                                                       |
| regex_v8                 | 26.6 ms                                                      | 23.6 ms: 1.13x faster                                                       |
| pathlib                  | 21.7 ms                                                      | 19.4 ms: 1.12x faster                                                       |
| xml_etree_generate       | 94.6 ms                                                      | 86.5 ms: 1.09x faster                                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.67 ms: 1.09x faster                                                       |
| sqlite_synth             | 2.97 us                                                      | 2.76 us: 1.08x faster                                                       |
| regex_dna                | 259 ms                                                       | 242 ms: 1.07x faster                                                        |
| async_generators         | 422 ms                                                       | 396 ms: 1.07x faster                                                        |
| xml_etree_parse          | 162 ms                                                       | 152 ms: 1.06x faster                                                        |
| meteor_contest           | 137 ms                                                       | 131 ms: 1.04x faster                                                        |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.03x faster                                                        |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                                       |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.02x slower                                                       |
| gc_traversal             | 3.45 ms                                                      | 3.54 ms: 1.03x slower                                                       |
| unpickle                 | 14.2 us                                                      | 14.7 us: 1.04x slower                                                       |
| unpickle_list            | 4.49 us                                                      | 4.69 us: 1.04x slower                                                       |
| pickle_dict              | 30.0 us                                                      | 32.6 us: 1.09x slower                                                       |
| pickle_list              | 4.11 us                                                      | 4.54 us: 1.11x slower                                                       |
| telco                    | 7.14 ms                                                      | 8.00 ms: 1.12x slower                                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.63 ms: 1.18x slower                                                       |
| regex_effbot             | 2.99 ms                                                      | 3.77 ms: 1.26x slower                                                       |
| dask                     | 463 ms                                                       | 588 ms: 1.27x slower                                                        |
| coverage                 | 64.0 ms                                                      | 88.4 ms: 1.38x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
