
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2cd1c87
- commit date: 2023-05-14
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                         |
| docutils       | 3.40 sec                                                     | 2.87 sec: 1.18x faster                                       |
| tornado_http   | 152 ms                                                       | 112 ms: 1.35x faster                                         |
| Geometric mean | (ref)                                                        | 1.26x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 86.2 ms: 1.59x faster                                        |
| float          | 110 ms                                                       | 79.0 ms: 1.40x faster                                        |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.32x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.34x faster                                         |
| regex_v8       | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                        |
| regex_dna      | 259 ms                                                       | 228 ms: 1.14x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                        |
| Geometric mean | (ref)                                                        | 1.12x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 201 us: 1.60x faster                                         |
| pickle_pure_python   | 457 us                                                       | 321 us: 1.43x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                        |
| tomli_loads          | 2.97 sec                                                     | 2.20 sec: 1.35x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 59.1 ms: 1.29x faster                                        |
| json_loads           | 30.0 us                                                      | 24.0 us: 1.25x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 86.0 ms: 1.10x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 148 ms: 1.09x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pickle               | 9.94 us                                                      | 10.2 us: 1.02x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.61 us: 1.03x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.29 us: 1.04x slower                                        |
| unpickle             | 14.2 us                                                      | 14.9 us: 1.05x slower                                        |
| pickle_dict          | 30.0 us                                                      | 32.8 us: 1.09x slower                                        |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.40 ms: 1.15x slower                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.96 ms: 1.47x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 157 us: 3.33x faster                                         |
| deltablue                | 7.47 ms                                                      | 3.26 ms: 2.29x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 379 ms: 2.06x faster                                         |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                       |
| logging_silent           | 166 ns                                                       | 91.9 ns: 1.80x faster                                        |
| go                       | 259 ms                                                       | 147 ms: 1.76x faster                                         |
| richards_super           | 90.8 ms                                                      | 51.6 ms: 1.76x faster                                        |
| chaos                    | 107 ms                                                       | 64.3 ms: 1.67x faster                                        |
| scimark_lu               | 164 ms                                                       | 99.7 ms: 1.64x faster                                        |
| hexiom                   | 9.52 ms                                                      | 5.82 ms: 1.64x faster                                        |
| sqlglot_parse            | 2.26 ms                                                      | 1.38 ms: 1.63x faster                                        |
| richards                 | 74.1 ms                                                      | 45.4 ms: 1.63x faster                                        |
| scimark_sor              | 177 ms                                                       | 110 ms: 1.61x faster                                         |
| unpickle_pure_python     | 321 us                                                       | 201 us: 1.60x faster                                         |
| nbody                    | 137 ms                                                       | 86.2 ms: 1.59x faster                                        |
| generators               | 58.0 ms                                                      | 36.4 ms: 1.59x faster                                        |
| raytrace                 | 488 ms                                                       | 307 ms: 1.59x faster                                         |
| scimark_monte_carlo      | 109 ms                                                       | 69.0 ms: 1.59x faster                                        |
| pyflate                  | 697 ms                                                       | 443 ms: 1.57x faster                                         |
| async_tree_io            | 1.61 sec                                                     | 1.05 sec: 1.53x faster                                       |
| async_tree_none          | 700 ms                                                       | 458 ms: 1.53x faster                                         |
| sqlglot_transpile        | 2.71 ms                                                      | 1.78 ms: 1.52x faster                                        |
| spectral_norm            | 136 ms                                                       | 90.9 ms: 1.50x faster                                        |
| async_tree_memoization   | 824 ms                                                       | 552 ms: 1.49x faster                                         |
| crypto_pyaes             | 118 ms                                                       | 80.1 ms: 1.48x faster                                        |
| mako                     | 14.7 ms                                                      | 9.96 ms: 1.47x faster                                        |
| pickle_pure_python       | 457 us                                                       | 321 us: 1.43x faster                                         |
| fannkuch                 | 496 ms                                                       | 349 ms: 1.42x faster                                         |
| float                    | 110 ms                                                       | 79.0 ms: 1.40x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 698 ms: 1.36x faster                                         |
| coroutines               | 30.4 ms                                                      | 22.5 ms: 1.35x faster                                        |
| tornado_http             | 152 ms                                                       | 112 ms: 1.35x faster                                         |
| tomli_loads              | 2.97 sec                                                     | 2.20 sec: 1.35x faster                                       |
| deepcopy_memo            | 48.9 us                                                      | 36.3 us: 1.35x faster                                        |
| regex_compile            | 194 ms                                                       | 144 ms: 1.34x faster                                         |
| pycparser                | 1.66 sec                                                     | 1.25 sec: 1.33x faster                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                       |
| logging_simple           | 8.90 us                                                      | 6.75 us: 1.32x faster                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 798 ms: 1.32x faster                                         |
| mypy2                    | 466 ms                                                       | 362 ms: 1.29x faster                                         |
| xml_etree_process        | 76.0 ms                                                      | 59.1 ms: 1.29x faster                                        |
| logging_format           | 9.57 us                                                      | 7.46 us: 1.28x faster                                        |
| nqueens                  | 112 ms                                                       | 90.0 ms: 1.25x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                         |
| json_loads               | 30.0 us                                                      | 24.0 us: 1.25x faster                                        |
| bench_mp_pool            | 7.18 ms                                                      | 5.80 ms: 1.24x faster                                        |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                         |
| comprehensions           | 26.9 us                                                      | 21.9 us: 1.23x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 65.1 ms: 1.23x faster                                        |
| sqlglot_optimize         | 70.3 ms                                                      | 57.7 ms: 1.22x faster                                        |
| deepcopy                 | 454 us                                                       | 375 us: 1.21x faster                                         |
| mdp                      | 3.03 sec                                                     | 2.52 sec: 1.20x faster                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.38 us: 1.19x faster                                        |
| docutils                 | 3.40 sec                                                     | 2.87 sec: 1.18x faster                                       |
| bench_thread_pool        | 1.14 ms                                                      | 960 us: 1.18x faster                                         |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.41 ms: 1.18x faster                                        |
| json                     | 5.96 ms                                                      | 5.09 ms: 1.17x faster                                        |
| unpack_sequence          | 59.5 ns                                                      | 51.2 ns: 1.16x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                        |
| scimark_fft              | 359 ms                                                       | 312 ms: 1.15x faster                                         |
| regex_dna                | 259 ms                                                       | 228 ms: 1.14x faster                                         |
| sqlite_synth             | 2.97 us                                                      | 2.65 us: 1.12x faster                                        |
| pathlib                  | 21.7 ms                                                      | 19.5 ms: 1.11x faster                                        |
| xml_etree_generate       | 94.6 ms                                                      | 86.0 ms: 1.10x faster                                        |
| async_generators         | 422 ms                                                       | 386 ms: 1.09x faster                                         |
| create_gc_cycles         | 1.82 ms                                                      | 1.66 ms: 1.09x faster                                        |
| xml_etree_parse          | 162 ms                                                       | 148 ms: 1.09x faster                                         |
| meteor_contest           | 137 ms                                                       | 127 ms: 1.08x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                        |
| telco                    | 7.14 ms                                                      | 7.08 ms: 1.01x faster                                        |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.02x slower                                        |
| unpickle_list            | 4.49 us                                                      | 4.61 us: 1.03x slower                                        |
| pickle_list              | 4.11 us                                                      | 4.29 us: 1.04x slower                                        |
| unpickle                 | 14.2 us                                                      | 14.9 us: 1.05x slower                                        |
| pickle_dict              | 30.0 us                                                      | 32.8 us: 1.09x slower                                        |
| python_startup_no_site   | 7.32 ms                                                      | 8.40 ms: 1.15x slower                                        |
| regex_effbot             | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                        |
| gc_traversal             | 3.45 ms                                                      | 4.05 ms: 1.17x slower                                        |
| dask                     | 463 ms                                                       | 555 ms: 1.20x slower                                         |
| coverage                 | 64.0 ms                                                      | 93.3 ms: 1.46x slower                                        |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                 |
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
