
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 5113ed7
- commit date: 2023-07-29
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                      |
| tornado_http   | 152 ms                                                       | 120 ms: 1.27x faster                                        |
| Geometric mean | (ref)                                                        | 1.22x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 88.4 ms: 1.55x faster                                       |
| float          | 110 ms                                                       | 81.1 ms: 1.36x faster                                       |
| pidigits       | 271 ms                                                       | 259 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 150 ms: 1.29x faster                                        |
| regex_v8       | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                       |
| regex_dna      | 259 ms                                                       | 245 ms: 1.06x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.48 ms: 1.16x slower                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 318 us: 1.44x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                       |
| unpickle_pure_python | 321 us                                                       | 239 us: 1.34x faster                                        |
| xml_etree_process    | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.32 sec: 1.28x faster                                      |
| json_loads           | 30.0 us                                                      | 24.8 us: 1.21x faster                                       |
| xml_etree_generate   | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.05x faster                                        |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                       |
| unpickle             | 14.2 us                                                      | 14.5 us: 1.02x slower                                       |
| pickle_dict          | 30.0 us                                                      | 31.7 us: 1.06x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.82 us: 1.07x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.43 us: 1.08x slower                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.63 ms: 1.18x slower                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf2-x86_64-python-main-3.13.0a0-5113ed7 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.41x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 368 ms: 2.13x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.73 ms: 2.00x faster                                       |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                      |
| raytrace                 | 488 ms                                                       | 283 ms: 1.73x faster                                        |
| chaos                    | 107 ms                                                       | 62.3 ms: 1.72x faster                                       |
| logging_silent           | 166 ns                                                       | 97.3 ns: 1.70x faster                                       |
| scimark_lu               | 164 ms                                                       | 97.4 ms: 1.68x faster                                       |
| crypto_pyaes             | 118 ms                                                       | 73.2 ms: 1.62x faster                                       |
| scimark_monte_carlo      | 109 ms                                                       | 68.2 ms: 1.60x faster                                       |
| generators               | 58.0 ms                                                      | 36.7 ms: 1.58x faster                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.44 ms: 1.56x faster                                       |
| nbody                    | 137 ms                                                       | 88.4 ms: 1.55x faster                                       |
| bench_mp_pool            | 7.18 ms                                                      | 4.65 ms: 1.54x faster                                       |
| go                       | 259 ms                                                       | 173 ms: 1.50x faster                                        |
| async_tree_none          | 700 ms                                                       | 473 ms: 1.48x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.09 sec: 1.47x faster                                      |
| sqlglot_transpile        | 2.71 ms                                                      | 1.85 ms: 1.47x faster                                       |
| hexiom                   | 9.52 ms                                                      | 6.51 ms: 1.46x faster                                       |
| richards_super           | 90.8 ms                                                      | 62.3 ms: 1.46x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 571 ms: 1.44x faster                                        |
| pickle_pure_python       | 457 us                                                       | 318 us: 1.44x faster                                        |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                       |
| spectral_norm            | 136 ms                                                       | 97.1 ms: 1.40x faster                                       |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                       |
| float                    | 110 ms                                                       | 81.1 ms: 1.36x faster                                       |
| pyflate                  | 697 ms                                                       | 516 ms: 1.35x faster                                        |
| unpickle_pure_python     | 321 us                                                       | 239 us: 1.34x faster                                        |
| richards                 | 74.1 ms                                                      | 55.2 ms: 1.34x faster                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 718 ms: 1.32x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 802 ms: 1.31x faster                                        |
| coroutines               | 30.4 ms                                                      | 23.4 ms: 1.30x faster                                       |
| xml_etree_process        | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                       |
| deepcopy_memo            | 48.9 us                                                      | 37.8 us: 1.29x faster                                       |
| regex_compile            | 194 ms                                                       | 150 ms: 1.29x faster                                        |
| logging_simple           | 8.90 us                                                      | 6.92 us: 1.29x faster                                       |
| tomli_loads              | 2.97 sec                                                     | 2.32 sec: 1.28x faster                                      |
| logging_format           | 9.57 us                                                      | 7.50 us: 1.28x faster                                       |
| unpack_sequence          | 59.5 ns                                                      | 47.0 ns: 1.27x faster                                       |
| tornado_http             | 152 ms                                                       | 120 ms: 1.27x faster                                        |
| mypy2                    | 466 ms                                                       | 373 ms: 1.25x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.25x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.34 sec: 1.24x faster                                      |
| scimark_sor              | 177 ms                                                       | 144 ms: 1.23x faster                                        |
| fannkuch                 | 496 ms                                                       | 404 ms: 1.23x faster                                        |
| nqueens                  | 112 ms                                                       | 92.1 ms: 1.22x faster                                       |
| comprehensions           | 26.9 us                                                      | 22.1 us: 1.22x faster                                       |
| json_loads               | 30.0 us                                                      | 24.8 us: 1.21x faster                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.30 ms: 1.21x faster                                       |
| deepcopy                 | 454 us                                                       | 377 us: 1.20x faster                                        |
| mdp                      | 3.03 sec                                                     | 2.54 sec: 1.20x faster                                      |
| bench_thread_pool        | 1.14 ms                                                      | 950 us: 1.20x faster                                        |
| sqlglot_optimize         | 70.3 ms                                                      | 58.8 ms: 1.19x faster                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.42 us: 1.18x faster                                       |
| docutils                 | 3.40 sec                                                     | 2.90 sec: 1.17x faster                                      |
| scimark_fft              | 359 ms                                                       | 306 ms: 1.17x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 68.5 ms: 1.17x faster                                       |
| json                     | 5.96 ms                                                      | 5.19 ms: 1.15x faster                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.62 ms: 1.12x faster                                       |
| xml_etree_generate       | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                       |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                        |
| sqlite_synth             | 2.97 us                                                      | 2.70 us: 1.10x faster                                       |
| regex_v8                 | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                       |
| pathlib                  | 21.7 ms                                                      | 19.9 ms: 1.09x faster                                       |
| async_generators         | 422 ms                                                       | 393 ms: 1.07x faster                                        |
| regex_dna                | 259 ms                                                       | 245 ms: 1.06x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.05x faster                                        |
| meteor_contest           | 137 ms                                                       | 131 ms: 1.04x faster                                        |
| pidigits                 | 271 ms                                                       | 259 ms: 1.04x faster                                        |
| gc_traversal             | 3.45 ms                                                      | 3.48 ms: 1.01x slower                                       |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                       |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.02x slower                                       |
| unpickle                 | 14.2 us                                                      | 14.5 us: 1.02x slower                                       |
| pickle_dict              | 30.0 us                                                      | 31.7 us: 1.06x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.82 us: 1.07x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.43 us: 1.08x slower                                       |
| telco                    | 7.14 ms                                                      | 7.94 ms: 1.11x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.48 ms: 1.16x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.63 ms: 1.18x slower                                       |
| dask                     | 463 ms                                                       | 586 ms: 1.27x slower                                        |
| coverage                 | 64.0 ms                                                      | 92.0 ms: 1.44x slower                                       |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
