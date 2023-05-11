
# Results vs. 3.10.4

- fork: python
- ref: e629ab6adf19544d5ee3
- machine: linux-x86_64
- commit hash: e629ab6
- commit date: 2023-05-11
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 283 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                       |
| tornado_http   | 151 ms                                                       | 114 ms: 1.32x faster                                                         |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 84.2 ms: 1.57x faster                                                        |
| float          | 109 ms                                                       | 79.9 ms: 1.37x faster                                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 145 ms: 1.32x faster                                                         |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 24.3 ms: 1.07x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.55 ms: 1.19x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 206 us: 1.55x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 323 us: 1.40x faster                                                         |
| json_dumps           | 14.3 ms                                                      | 10.3 ms: 1.39x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 59.0 ms: 1.32x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 86.0 ms: 1.09x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 150 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 109 ms                                                       | 107 ms: 1.02x faster                                                         |
| pickle               | 10.1 us                                                      | 10.0 us: 1.01x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.81 us: 1.02x slower                                                        |
| pickle_list          | 4.11 us                                                      | 4.33 us: 1.05x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 31.9 us: 1.08x slower                                                        |
| unpickle             | 13.3 us                                                      | 14.8 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.43 ms: 1.15x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.84 ms: 1.50x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-pythonperf2-x86_64-python-e629ab6adf19544d5ee3-3.12.0a7+-e629ab6 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.25 ms: 2.32x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 379 ms: 2.08x faster                                                         |
| go                      | 264 ms                                                       | 152 ms: 1.73x faster                                                         |
| logging_silent          | 165 ns                                                       | 96.0 ns: 1.71x faster                                                        |
| chaos                   | 108 ms                                                       | 64.8 ms: 1.66x faster                                                        |
| raytrace                | 491 ms                                                       | 297 ms: 1.66x faster                                                         |
| scimark_lu              | 164 ms                                                       | 99.4 ms: 1.65x faster                                                        |
| pyflate                 | 731 ms                                                       | 444 ms: 1.65x faster                                                         |
| richards                | 73.9 ms                                                      | 44.9 ms: 1.64x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.38 ms: 1.63x faster                                                        |
| hexiom                  | 9.54 ms                                                      | 5.85 ms: 1.63x faster                                                        |
| scimark_sor             | 177 ms                                                       | 111 ms: 1.60x faster                                                         |
| nbody                   | 132 ms                                                       | 84.2 ms: 1.57x faster                                                        |
| generators              | 57.0 ms                                                      | 36.5 ms: 1.56x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 206 us: 1.55x faster                                                         |
| async_tree_io           | 1.61 sec                                                     | 1.05 sec: 1.54x faster                                                       |
| async_tree_none         | 698 ms                                                       | 456 ms: 1.53x faster                                                         |
| spectral_norm           | 138 ms                                                       | 90.5 ms: 1.52x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.78 ms: 1.51x faster                                                        |
| mako                    | 14.7 ms                                                      | 9.84 ms: 1.50x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 549 ms: 1.50x faster                                                         |
| crypto_pyaes            | 119 ms                                                       | 80.2 ms: 1.48x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 73.6 ms: 1.48x faster                                                        |
| fannkuch                | 496 ms                                                       | 345 ms: 1.44x faster                                                         |
| pickle_pure_python      | 451 us                                                       | 323 us: 1.40x faster                                                         |
| json_dumps              | 14.3 ms                                                      | 10.3 ms: 1.39x faster                                                        |
| logging_simple          | 9.24 us                                                      | 6.66 us: 1.39x faster                                                        |
| float                   | 109 ms                                                       | 79.9 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 697 ms: 1.37x faster                                                         |
| logging_format          | 9.94 us                                                      | 7.30 us: 1.36x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 36.4 us: 1.35x faster                                                        |
| coroutines              | 30.6 ms                                                      | 22.8 ms: 1.34x faster                                                        |
| tornado_http            | 151 ms                                                       | 114 ms: 1.32x faster                                                         |
| regex_compile           | 191 ms                                                       | 145 ms: 1.32x faster                                                         |
| xml_etree_process       | 77.6 ms                                                      | 59.0 ms: 1.32x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.28 sec: 1.30x faster                                                       |
| pprint_pformat          | 2.12 sec                                                     | 1.66 sec: 1.28x faster                                                       |
| mypy2                   | 466 ms                                                       | 367 ms: 1.27x faster                                                         |
| pprint_safe_repr        | 1.03 sec                                                     | 813 ms: 1.26x faster                                                         |
| sqlglot_normalize       | 147 ms                                                       | 117 ms: 1.25x faster                                                         |
| 2to3                    | 352 ms                                                       | 283 ms: 1.24x faster                                                         |
| comprehensions          | 27.3 us                                                      | 22.0 us: 1.24x faster                                                        |
| json_loads              | 30.3 us                                                      | 24.5 us: 1.24x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 65.7 ms: 1.23x faster                                                        |
| nqueens                 | 114 ms                                                       | 92.8 ms: 1.22x faster                                                        |
| deepcopy                | 457 us                                                       | 376 us: 1.22x faster                                                         |
| sqlglot_optimize        | 70.1 ms                                                      | 58.4 ms: 1.20x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 5.93 ms: 1.20x faster                                                        |
| scimark_fft             | 359 ms                                                       | 302 ms: 1.19x faster                                                         |
| bench_thread_pool       | 1.14 ms                                                      | 960 us: 1.19x faster                                                         |
| docutils                | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.41 ms: 1.16x faster                                                        |
| json                    | 5.94 ms                                                      | 5.18 ms: 1.15x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.42 us: 1.14x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.58 sec: 1.14x faster                                                       |
| unpack_sequence         | 59.7 ns                                                      | 52.9 ns: 1.13x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.64 us: 1.12x faster                                                        |
| regex_dna               | 261 ms                                                       | 234 ms: 1.12x faster                                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.63 ms: 1.10x faster                                                        |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                                         |
| xml_etree_generate      | 94.1 ms                                                      | 86.0 ms: 1.09x faster                                                        |
| async_generators        | 419 ms                                                       | 385 ms: 1.09x faster                                                         |
| regex_v8                | 26.0 ms                                                      | 24.3 ms: 1.07x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 150 ms: 1.07x faster                                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| pathlib                 | 21.3 ms                                                      | 20.7 ms: 1.03x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 107 ms: 1.02x faster                                                         |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                        |
| pickle                  | 10.1 us                                                      | 10.0 us: 1.01x faster                                                        |
| telco                   | 7.14 ms                                                      | 7.11 ms: 1.00x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.81 us: 1.02x slower                                                        |
| pickle_list             | 4.11 us                                                      | 4.33 us: 1.05x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 31.9 us: 1.08x slower                                                        |
| unpickle                | 13.3 us                                                      | 14.8 us: 1.12x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.43 ms: 1.15x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 4.06 ms: 1.17x slower                                                        |
| dask                    | 478 ms                                                       | 562 ms: 1.17x slower                                                         |
| regex_effbot            | 2.99 ms                                                      | 3.55 ms: 1.19x slower                                                        |
| coverage                | 71.1 ms                                                      | 94.6 ms: 1.33x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                                 |
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
