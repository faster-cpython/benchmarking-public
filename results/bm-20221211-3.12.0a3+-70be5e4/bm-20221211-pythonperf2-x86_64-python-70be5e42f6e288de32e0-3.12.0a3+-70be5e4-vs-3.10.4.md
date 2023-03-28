
# Results vs. 3.10.4

- fork: python
- ref: 70be5e42f6e288de32e0
- machine: linux-x86_64
- commit hash: 70be5e4
- commit date: 2022-12-11
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 281 ms: 1.25x faster                                                         |
| chameleon      | 9.62 ms                                                      | 7.48 ms: 1.29x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                                       |
| html5lib       | 96.3 ms                                                      | 67.6 ms: 1.42x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.3 ms: 1.49x faster                                                        |
| nbody          | 132 ms                                                       | 89.3 ms: 1.48x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 150 ms: 1.27x faster                                                         |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 23.7 ms: 1.10x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.43 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 216 us: 1.47x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 311 us: 1.45x faster                                                         |
| xml_etree_process    | 77.6 ms                                                      | 54.3 ms: 1.43x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 10.3 ms: 1.39x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.0 us: 1.26x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 79.5 ms: 1.18x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.70 us: 1.11x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.33 us: 1.09x faster                                                        |
| pickle               | 10.1 us                                                      | 9.71 us: 1.04x faster                                                        |
| unpickle             | 13.3 us                                                      | 13.0 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 107 ms: 1.02x faster                                                         |
| pickle_dict          | 29.5 us                                                      | 31.6 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| django_template | 52.0 ms                                                      | 39.6 ms: 1.31x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 24.4 ms: 1.30x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 53.1 ms: 1.20x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.73 ms: 2.02x faster                                                        |
| pyflate                 | 731 ms                                                       | 437 ms: 1.68x faster                                                         |
| scimark_sor             | 177 ms                                                       | 106 ms: 1.67x faster                                                         |
| logging_silent          | 165 ns                                                       | 99.3 ns: 1.66x faster                                                        |
| scimark_lu              | 164 ms                                                       | 101 ms: 1.62x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 67.5 ms: 1.61x faster                                                        |
| go                      | 264 ms                                                       | 167 ms: 1.58x faster                                                         |
| richards                | 73.9 ms                                                      | 47.0 ms: 1.57x faster                                                        |
| raytrace                | 491 ms                                                       | 320 ms: 1.54x faster                                                         |
| bench_mp_pool           | 7.10 ms                                                      | 4.63 ms: 1.53x faster                                                        |
| float                   | 109 ms                                                       | 73.3 ms: 1.49x faster                                                        |
| nbody                   | 132 ms                                                       | 89.3 ms: 1.48x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 216 us: 1.47x faster                                                         |
| sqlglot_parse           | 2.24 ms                                                      | 1.53 ms: 1.46x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 311 us: 1.45x faster                                                         |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| spectral_norm           | 138 ms                                                       | 95.6 ms: 1.44x faster                                                        |
| xml_etree_process       | 77.6 ms                                                      | 54.3 ms: 1.43x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.89 ms: 1.43x faster                                                        |
| html5lib                | 96.3 ms                                                      | 67.6 ms: 1.42x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 84.0 ms: 1.41x faster                                                        |
| chaos                   | 108 ms                                                       | 77.2 ms: 1.40x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.3 ms: 1.39x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 6.94 ms: 1.37x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.74 ms: 1.36x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 36.2 us: 1.36x faster                                                        |
| thrift                  | 1.23 ms                                                      | 905 us: 1.35x faster                                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.58 sec: 1.35x faster                                                       |
| logging_simple          | 9.24 us                                                      | 6.87 us: 1.34x faster                                                        |
| async_tree_none         | 698 ms                                                       | 520 ms: 1.34x faster                                                         |
| async_tree_memoization  | 822 ms                                                       | 618 ms: 1.33x faster                                                         |
| pprint_safe_repr        | 1.03 sec                                                     | 771 ms: 1.33x faster                                                         |
| django_template         | 52.0 ms                                                      | 39.6 ms: 1.31x faster                                                        |
| logging_format          | 9.94 us                                                      | 7.59 us: 1.31x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 45.7 ns: 1.31x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 24.4 ms: 1.30x faster                                                        |
| scimark_fft             | 359 ms                                                       | 278 ms: 1.29x faster                                                         |
| chameleon               | 9.62 ms                                                      | 7.48 ms: 1.29x faster                                                        |
| async_generators        | 419 ms                                                       | 328 ms: 1.28x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.30 sec: 1.28x faster                                                       |
| regex_compile           | 191 ms                                                       | 150 ms: 1.27x faster                                                         |
| json_loads              | 30.3 us                                                      | 24.0 us: 1.26x faster                                                        |
| 2to3                    | 352 ms                                                       | 281 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed | 951 ms                                                       | 760 ms: 1.25x faster                                                         |
| mypy2                   | 466 ms                                                       | 373 ms: 1.25x faster                                                         |
| docutils                | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                                       |
| deepcopy                | 457 us                                                       | 373 us: 1.23x faster                                                         |
| fannkuch                | 496 ms                                                       | 405 ms: 1.22x faster                                                         |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.22x faster                                                         |
| dulwich_log             | 80.5 ms                                                      | 66.7 ms: 1.21x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 58.1 ms: 1.21x faster                                                        |
| genshi_xml              | 63.5 ms                                                      | 53.1 ms: 1.20x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 79.5 ms: 1.18x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 963 us: 1.18x faster                                                         |
| json                    | 5.94 ms                                                      | 5.04 ms: 1.18x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.33 us: 1.17x faster                                                        |
| nqueens                 | 114 ms                                                       | 98.2 ms: 1.16x faster                                                        |
| dask                    | 478 ms                                                       | 413 ms: 1.16x faster                                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.58 ms: 1.14x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 141 ms: 1.14x faster                                                         |
| sqlite_synth            | 2.96 us                                                      | 2.61 us: 1.14x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 18.8 ms: 1.13x faster                                                        |
| sympy_expand            | 603 ms                                                       | 541 ms: 1.11x faster                                                         |
| mdp                     | 2.95 sec                                                     | 2.65 sec: 1.11x faster                                                       |
| pickle_list             | 4.11 us                                                      | 3.70 us: 1.11x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 709 ms: 1.11x faster                                                         |
| regex_dna               | 261 ms                                                       | 236 ms: 1.11x faster                                                         |
| coroutines              | 30.6 ms                                                      | 27.7 ms: 1.10x faster                                                        |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                                         |
| regex_v8                | 26.0 ms                                                      | 23.7 ms: 1.10x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.33 us: 1.09x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.7 ms: 1.09x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.56 ms: 1.09x faster                                                        |
| pidigits                | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| sympy_str               | 358 ms                                                       | 335 ms: 1.07x faster                                                         |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                        |
| pickle                  | 10.1 us                                                      | 9.71 us: 1.04x faster                                                        |
| unpickle                | 13.3 us                                                      | 13.0 us: 1.02x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 107 ms: 1.02x faster                                                         |
| sympy_sum               | 193 ms                                                       | 189 ms: 1.02x faster                                                         |
| comprehensions          | 27.3 us                                                      | 26.8 us: 1.02x faster                                                        |
| pickle_dict             | 29.5 us                                                      | 31.6 us: 1.07x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| generators              | 57.0 ms                                                      | 61.2 ms: 1.07x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.75 ms: 1.08x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.43 ms: 1.15x slower                                                        |
| coverage                | 71.1 ms                                                      | 86.1 ms: 1.21x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                 |
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
