
# Results vs. 3.10.4

- fork: python
- ref: 872cbc613245db7a1fc5
- machine: linux-x86_64
- commit hash: 872cbc6
- commit date: 2023-05-02
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 285 ms: 1.23x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| html5lib       | 96.3 ms                                                      | 70.2 ms: 1.37x faster                                                        |
| tornado_http   | 151 ms                                                       | 113 ms: 1.34x faster                                                         |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 86.2 ms: 1.53x faster                                                        |
| float          | 109 ms                                                       | 79.4 ms: 1.38x faster                                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 144 ms: 1.32x faster                                                         |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 23.9 ms: 1.09x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 208 us: 1.53x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 321 us: 1.41x faster                                                         |
| json_dumps           | 14.3 ms                                                      | 10.4 ms: 1.37x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 58.5 ms: 1.33x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 86.3 ms: 1.09x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 148 ms: 1.08x faster                                                         |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| pickle               | 10.1 us                                                      | 10.3 us: 1.02x slower                                                        |
| unpickle_list        | 4.73 us                                                      | 4.87 us: 1.03x slower                                                        |
| pickle_list          | 4.11 us                                                      | 4.29 us: 1.04x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 31.5 us: 1.07x slower                                                        |
| unpickle             | 13.3 us                                                      | 15.0 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.37 ms: 1.14x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| genshi_text    | 31.7 ms                                                      | 24.4 ms: 1.30x faster                                                        |
| genshi_xml     | 63.5 ms                                                      | 54.3 ms: 1.17x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.22 ms: 2.34x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 377 ms: 2.09x faster                                                         |
| go                      | 264 ms                                                       | 148 ms: 1.78x faster                                                         |
| richards                | 73.9 ms                                                      | 43.2 ms: 1.71x faster                                                        |
| scimark_lu              | 164 ms                                                       | 98.7 ms: 1.66x faster                                                        |
| logging_silent          | 165 ns                                                       | 99.5 ns: 1.65x faster                                                        |
| pyflate                 | 731 ms                                                       | 444 ms: 1.65x faster                                                         |
| chaos                   | 108 ms                                                       | 67.1 ms: 1.61x faster                                                        |
| raytrace                | 491 ms                                                       | 306 ms: 1.61x faster                                                         |
| sqlglot_parse           | 2.24 ms                                                      | 1.40 ms: 1.60x faster                                                        |
| hexiom                  | 9.54 ms                                                      | 5.98 ms: 1.60x faster                                                        |
| generators              | 57.0 ms                                                      | 36.2 ms: 1.58x faster                                                        |
| scimark_sor             | 177 ms                                                       | 113 ms: 1.56x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 70.4 ms: 1.54x faster                                                        |
| nbody                   | 132 ms                                                       | 86.2 ms: 1.53x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 208 us: 1.53x faster                                                         |
| spectral_norm           | 138 ms                                                       | 91.3 ms: 1.51x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.81 ms: 1.49x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.10 sec: 1.47x faster                                                       |
| async_tree_none         | 698 ms                                                       | 480 ms: 1.46x faster                                                         |
| crypto_pyaes            | 119 ms                                                       | 81.5 ms: 1.45x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| fannkuch                | 496 ms                                                       | 345 ms: 1.44x faster                                                         |
| async_tree_memoization  | 822 ms                                                       | 577 ms: 1.43x faster                                                         |
| pickle_pure_python      | 451 us                                                       | 321 us: 1.41x faster                                                         |
| float                   | 109 ms                                                       | 79.4 ms: 1.38x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 5.16 ms: 1.38x faster                                                        |
| logging_simple          | 9.24 us                                                      | 6.71 us: 1.38x faster                                                        |
| html5lib                | 96.3 ms                                                      | 70.2 ms: 1.37x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.4 ms: 1.37x faster                                                        |
| logging_format          | 9.94 us                                                      | 7.34 us: 1.35x faster                                                        |
| tornado_http            | 151 ms                                                       | 113 ms: 1.34x faster                                                         |
| thrift                  | 1.23 ms                                                      | 917 us: 1.34x faster                                                         |
| coroutines              | 30.6 ms                                                      | 22.9 ms: 1.33x faster                                                        |
| xml_etree_process       | 77.6 ms                                                      | 58.5 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 717 ms: 1.33x faster                                                         |
| regex_compile           | 191 ms                                                       | 144 ms: 1.32x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.27 sec: 1.30x faster                                                       |
| genshi_text             | 31.7 ms                                                      | 24.4 ms: 1.30x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 38.4 us: 1.28x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.66 sec: 1.28x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 806 ms: 1.27x faster                                                         |
| nqueens                 | 114 ms                                                       | 89.5 ms: 1.27x faster                                                        |
| mypy2                   | 466 ms                                                       | 376 ms: 1.24x faster                                                         |
| 2to3                    | 352 ms                                                       | 285 ms: 1.23x faster                                                         |
| dulwich_log             | 80.5 ms                                                      | 65.6 ms: 1.23x faster                                                        |
| sqlglot_normalize       | 147 ms                                                       | 121 ms: 1.22x faster                                                         |
| json_loads              | 30.3 us                                                      | 25.0 us: 1.21x faster                                                        |
| deepcopy                | 457 us                                                       | 382 us: 1.20x faster                                                         |
| sqlglot_optimize        | 70.1 ms                                                      | 59.1 ms: 1.19x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.32 ms: 1.18x faster                                                        |
| scimark_fft             | 359 ms                                                       | 304 ms: 1.18x faster                                                         |
| genshi_xml              | 63.5 ms                                                      | 54.3 ms: 1.17x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 974 us: 1.17x faster                                                         |
| mdp                     | 2.95 sec                                                     | 2.55 sec: 1.16x faster                                                       |
| json                    | 5.94 ms                                                      | 5.17 ms: 1.15x faster                                                        |
| regex_dna               | 261 ms                                                       | 227 ms: 1.15x faster                                                         |
| unpack_sequence         | 59.7 ns                                                      | 52.3 ns: 1.14x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.49 us: 1.12x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.64 us: 1.12x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 19.3 ms: 1.10x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.65 ms: 1.09x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 23.9 ms: 1.09x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 86.3 ms: 1.09x faster                                                        |
| async_generators        | 419 ms                                                       | 385 ms: 1.09x faster                                                         |
| xml_etree_parse         | 160 ms                                                       | 148 ms: 1.08x faster                                                         |
| comprehensions          | 27.3 us                                                      | 25.2 us: 1.08x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                                        |
| meteor_contest          | 142 ms                                                       | 139 ms: 1.02x faster                                                         |
| telco                   | 7.14 ms                                                      | 7.17 ms: 1.00x slower                                                        |
| pickle                  | 10.1 us                                                      | 10.3 us: 1.02x slower                                                        |
| unpickle_list           | 4.73 us                                                      | 4.87 us: 1.03x slower                                                        |
| pickle_list             | 4.11 us                                                      | 4.29 us: 1.04x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 31.5 us: 1.07x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.80 ms: 1.10x slower                                                        |
| unpickle                | 13.3 us                                                      | 15.0 us: 1.13x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.37 ms: 1.14x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                                        |
| dask                    | 478 ms                                                       | 562 ms: 1.17x slower                                                         |
| coverage                | 71.1 ms                                                      | 89.9 ms: 1.27x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                 |
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum
