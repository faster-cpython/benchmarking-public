
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 4fe1c4b
- commit date: 2023-04-15
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                         |
| chameleon      | 9.62 ms                                                      | 7.49 ms: 1.28x faster                                        |
| docutils       | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                       |
| html5lib       | 96.3 ms                                                      | 68.4 ms: 1.41x faster                                        |
| tornado_http   | 151 ms                                                       | 114 ms: 1.32x faster                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 78.5 ms: 1.69x faster                                        |
| float          | 109 ms                                                       | 70.4 ms: 1.56x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.40x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 148 ms: 1.29x faster                                         |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                         |
| regex_v8       | 26.0 ms                                                      | 23.9 ms: 1.09x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 211 us: 1.51x faster                                         |
| pickle_pure_python   | 451 us                                                       | 321 us: 1.41x faster                                         |
| json_dumps           | 14.3 ms                                                      | 10.3 ms: 1.38x faster                                        |
| xml_etree_process    | 77.6 ms                                                      | 57.0 ms: 1.36x faster                                        |
| json_loads           | 30.3 us                                                      | 24.0 us: 1.26x faster                                        |
| xml_etree_generate   | 94.1 ms                                                      | 82.4 ms: 1.14x faster                                        |
| pickle_list          | 4.11 us                                                      | 3.74 us: 1.10x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.09x faster                                         |
| xml_etree_iterparse  | 109 ms                                                       | 101 ms: 1.08x faster                                         |
| unpickle_list        | 4.73 us                                                      | 4.63 us: 1.02x faster                                        |
| pickle               | 10.1 us                                                      | 9.98 us: 1.02x faster                                        |
| pickle_dict          | 29.5 us                                                      | 30.2 us: 1.02x slower                                        |
| unpickle             | 13.3 us                                                      | 14.2 us: 1.07x slower                                        |
| Geometric mean       | (ref)                                                        | 1.16x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.1 ms: 1.04x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.90 ms: 1.49x faster                                        |
| django_template | 52.0 ms                                                      | 41.3 ms: 1.26x faster                                        |
| genshi_text     | 31.7 ms                                                      | 25.8 ms: 1.23x faster                                        |
| genshi_xml      | 63.5 ms                                                      | 53.7 ms: 1.18x faster                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-pythonperf2-x86_64-python-main-3.12.0a7+-4fe1c4b |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.39 ms: 2.22x faster                                        |
| asyncio_tcp             | 787 ms                                                       | 383 ms: 2.05x faster                                         |
| logging_silent          | 165 ns                                                       | 94.1 ns: 1.75x faster                                        |
| nbody                   | 132 ms                                                       | 78.5 ms: 1.69x faster                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.34 ms: 1.68x faster                                        |
| raytrace                | 491 ms                                                       | 295 ms: 1.67x faster                                         |
| scimark_lu              | 164 ms                                                       | 100.0 ms: 1.64x faster                                       |
| scimark_monte_carlo     | 109 ms                                                       | 66.9 ms: 1.63x faster                                        |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.60x faster                                         |
| generators              | 57.0 ms                                                      | 35.6 ms: 1.60x faster                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.70 ms: 1.58x faster                                        |
| richards                | 73.9 ms                                                      | 47.3 ms: 1.56x faster                                        |
| pyflate                 | 731 ms                                                       | 469 ms: 1.56x faster                                         |
| float                   | 109 ms                                                       | 70.4 ms: 1.56x faster                                        |
| spectral_norm           | 138 ms                                                       | 89.6 ms: 1.54x faster                                        |
| go                      | 264 ms                                                       | 172 ms: 1.54x faster                                         |
| unpickle_pure_python    | 318 us                                                       | 211 us: 1.51x faster                                         |
| mako                    | 14.7 ms                                                      | 9.90 ms: 1.49x faster                                        |
| chaos                   | 108 ms                                                       | 72.9 ms: 1.48x faster                                        |
| hexiom                  | 9.54 ms                                                      | 6.63 ms: 1.44x faster                                        |
| crypto_pyaes            | 119 ms                                                       | 82.8 ms: 1.43x faster                                        |
| deepcopy_memo           | 49.2 us                                                      | 34.9 us: 1.41x faster                                        |
| html5lib                | 96.3 ms                                                      | 68.4 ms: 1.41x faster                                        |
| pickle_pure_python      | 451 us                                                       | 321 us: 1.41x faster                                         |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                       |
| json_dumps              | 14.3 ms                                                      | 10.3 ms: 1.38x faster                                        |
| scimark_fft             | 359 ms                                                       | 261 ms: 1.38x faster                                         |
| thrift                  | 1.23 ms                                                      | 899 us: 1.36x faster                                         |
| xml_etree_process       | 77.6 ms                                                      | 57.0 ms: 1.36x faster                                        |
| async_tree_none         | 698 ms                                                       | 515 ms: 1.36x faster                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.58 sec: 1.34x faster                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.80 ms: 1.34x faster                                        |
| logging_simple          | 9.24 us                                                      | 6.92 us: 1.33x faster                                        |
| async_tree_memoization  | 822 ms                                                       | 617 ms: 1.33x faster                                         |
| unpack_sequence         | 59.7 ns                                                      | 45.0 ns: 1.33x faster                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 773 ms: 1.33x faster                                         |
| tornado_http            | 151 ms                                                       | 114 ms: 1.32x faster                                         |
| bench_mp_pool           | 7.10 ms                                                      | 5.44 ms: 1.30x faster                                        |
| regex_compile           | 191 ms                                                       | 148 ms: 1.29x faster                                         |
| chameleon               | 9.62 ms                                                      | 7.49 ms: 1.28x faster                                        |
| logging_format          | 9.94 us                                                      | 7.80 us: 1.27x faster                                        |
| pycparser               | 1.66 sec                                                     | 1.30 sec: 1.27x faster                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 749 ms: 1.27x faster                                         |
| json_loads              | 30.3 us                                                      | 24.0 us: 1.26x faster                                        |
| django_template         | 52.0 ms                                                      | 41.3 ms: 1.26x faster                                        |
| fannkuch                | 496 ms                                                       | 395 ms: 1.26x faster                                         |
| sqlglot_normalize       | 147 ms                                                       | 118 ms: 1.25x faster                                         |
| dulwich_log             | 80.5 ms                                                      | 64.7 ms: 1.24x faster                                        |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                         |
| coroutines              | 30.6 ms                                                      | 24.7 ms: 1.24x faster                                        |
| genshi_text             | 31.7 ms                                                      | 25.8 ms: 1.23x faster                                        |
| mypy2                   | 466 ms                                                       | 379 ms: 1.23x faster                                         |
| docutils                | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                       |
| deepcopy                | 457 us                                                       | 377 us: 1.21x faster                                         |
| sqlglot_optimize        | 70.1 ms                                                      | 57.8 ms: 1.21x faster                                        |
| bench_thread_pool       | 1.14 ms                                                      | 962 us: 1.18x faster                                         |
| genshi_xml              | 63.5 ms                                                      | 53.7 ms: 1.18x faster                                        |
| json                    | 5.94 ms                                                      | 5.03 ms: 1.18x faster                                        |
| mdp                     | 2.95 sec                                                     | 2.52 sec: 1.17x faster                                       |
| pylint                  | 562 ms                                                       | 484 ms: 1.16x faster                                         |
| deepcopy_reduce         | 3.91 us                                                      | 3.41 us: 1.15x faster                                        |
| pathlib                 | 21.3 ms                                                      | 18.5 ms: 1.15x faster                                        |
| sqlite_synth            | 2.96 us                                                      | 2.58 us: 1.15x faster                                        |
| xml_etree_generate      | 94.1 ms                                                      | 82.4 ms: 1.14x faster                                        |
| nqueens                 | 114 ms                                                       | 100 ms: 1.14x faster                                         |
| meteor_contest          | 142 ms                                                       | 126 ms: 1.13x faster                                         |
| sympy_expand            | 603 ms                                                       | 537 ms: 1.12x faster                                         |
| regex_dna               | 261 ms                                                       | 234 ms: 1.12x faster                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.64 ms: 1.10x faster                                        |
| comprehensions          | 27.3 us                                                      | 24.8 us: 1.10x faster                                        |
| pickle_list             | 4.11 us                                                      | 3.74 us: 1.10x faster                                        |
| xml_etree_parse         | 160 ms                                                       | 146 ms: 1.09x faster                                         |
| regex_v8                | 26.0 ms                                                      | 23.9 ms: 1.09x faster                                        |
| sympy_str               | 358 ms                                                       | 331 ms: 1.08x faster                                         |
| xml_etree_iterparse     | 109 ms                                                       | 101 ms: 1.08x faster                                         |
| async_generators        | 419 ms                                                       | 388 ms: 1.08x faster                                         |
| telco                   | 7.14 ms                                                      | 6.76 ms: 1.06x faster                                        |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| python_startup          | 11.5 ms                                                      | 11.1 ms: 1.04x faster                                        |
| unpickle_list           | 4.73 us                                                      | 4.63 us: 1.02x faster                                        |
| pickle                  | 10.1 us                                                      | 9.98 us: 1.02x faster                                        |
| pickle_dict             | 29.5 us                                                      | 30.2 us: 1.02x slower                                        |
| gc_traversal            | 3.46 ms                                                      | 3.55 ms: 1.03x slower                                        |
| unpickle                | 13.3 us                                                      | 14.2 us: 1.07x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                        |
| dask                    | 478 ms                                                       | 564 ms: 1.18x slower                                         |
| coverage                | 71.1 ms                                                      | 91.1 ms: 1.28x slower                                        |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                 |
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
