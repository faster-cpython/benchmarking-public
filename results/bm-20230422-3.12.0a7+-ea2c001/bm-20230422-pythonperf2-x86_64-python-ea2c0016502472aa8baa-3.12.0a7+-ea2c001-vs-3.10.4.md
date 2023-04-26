
# Results vs. 3.10.4

- fork: python
- ref: ea2c0016502472aa8baa
- machine: linux-x86_64
- commit hash: ea2c001
- commit date: 2023-04-22
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                                         |
| chameleon      | 9.62 ms                                                      | 7.44 ms: 1.29x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| html5lib       | 96.3 ms                                                      | 68.9 ms: 1.40x faster                                                        |
| tornado_http   | 151 ms                                                       | 119 ms: 1.26x faster                                                         |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 83.7 ms: 1.58x faster                                                        |
| float          | 109 ms                                                       | 77.1 ms: 1.42x faster                                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 143 ms: 1.34x faster                                                         |
| regex_dna      | 261 ms                                                       | 230 ms: 1.14x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 23.6 ms: 1.10x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.40 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 209 us: 1.52x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 319 us: 1.42x faster                                                         |
| json_dumps           | 14.3 ms                                                      | 10.3 ms: 1.39x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 58.5 ms: 1.33x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.7 us: 1.23x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 85.2 ms: 1.10x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 151 ms: 1.06x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.95 us: 1.04x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.55 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 105 ms: 1.03x faster                                                         |
| pickle               | 10.1 us                                                      | 9.91 us: 1.02x faster                                                        |
| pickle_dict          | 29.5 us                                                      | 30.7 us: 1.04x slower                                                        |
| unpickle             | 13.3 us                                                      | 14.2 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.37 ms: 1.14x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                        |
| django_template | 52.0 ms                                                      | 38.3 ms: 1.36x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 25.0 ms: 1.27x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 53.9 ms: 1.18x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.30 ms: 2.28x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 379 ms: 2.08x faster                                                         |
| go                      | 264 ms                                                       | 146 ms: 1.81x faster                                                         |
| logging_silent          | 165 ns                                                       | 93.5 ns: 1.76x faster                                                        |
| scimark_lu              | 164 ms                                                       | 95.5 ms: 1.72x faster                                                        |
| richards                | 73.9 ms                                                      | 43.9 ms: 1.68x faster                                                        |
| raytrace                | 491 ms                                                       | 299 ms: 1.64x faster                                                         |
| sqlglot_parse           | 2.24 ms                                                      | 1.38 ms: 1.63x faster                                                        |
| chaos                   | 108 ms                                                       | 66.3 ms: 1.63x faster                                                        |
| hexiom                  | 9.54 ms                                                      | 5.92 ms: 1.61x faster                                                        |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.61x faster                                                         |
| spectral_norm           | 138 ms                                                       | 86.0 ms: 1.60x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 68.0 ms: 1.60x faster                                                        |
| pyflate                 | 731 ms                                                       | 458 ms: 1.60x faster                                                         |
| nbody                   | 132 ms                                                       | 83.7 ms: 1.58x faster                                                        |
| generators              | 57.0 ms                                                      | 36.6 ms: 1.56x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 209 us: 1.52x faster                                                         |
| sqlglot_transpile       | 2.69 ms                                                      | 1.78 ms: 1.51x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 79.0 ms: 1.50x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                        |
| float                   | 109 ms                                                       | 77.1 ms: 1.42x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 319 us: 1.42x faster                                                         |
| fannkuch                | 496 ms                                                       | 351 ms: 1.41x faster                                                         |
| async_tree_io           | 1.61 sec                                                     | 1.15 sec: 1.40x faster                                                       |
| logging_simple          | 9.24 us                                                      | 6.60 us: 1.40x faster                                                        |
| html5lib                | 96.3 ms                                                      | 68.9 ms: 1.40x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.3 ms: 1.39x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 594 ms: 1.38x faster                                                         |
| async_tree_none         | 698 ms                                                       | 505 ms: 1.38x faster                                                         |
| thrift                  | 1.23 ms                                                      | 887 us: 1.38x faster                                                         |
| logging_format          | 9.94 us                                                      | 7.32 us: 1.36x faster                                                        |
| django_template         | 52.0 ms                                                      | 38.3 ms: 1.36x faster                                                        |
| coroutines              | 30.6 ms                                                      | 22.7 ms: 1.35x faster                                                        |
| regex_compile           | 191 ms                                                       | 143 ms: 1.34x faster                                                         |
| xml_etree_process       | 77.6 ms                                                      | 58.5 ms: 1.33x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                                       |
| deepcopy_memo           | 49.2 us                                                      | 37.5 us: 1.31x faster                                                        |
| chameleon               | 9.62 ms                                                      | 7.44 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 739 ms: 1.29x faster                                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.65 sec: 1.29x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.01 ms: 1.27x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 25.0 ms: 1.27x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 811 ms: 1.27x faster                                                         |
| tornado_http            | 151 ms                                                       | 119 ms: 1.26x faster                                                         |
| nqueens                 | 114 ms                                                       | 90.1 ms: 1.26x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 65.0 ms: 1.24x faster                                                        |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                                         |
| scimark_fft             | 359 ms                                                       | 292 ms: 1.23x faster                                                         |
| json_loads              | 30.3 us                                                      | 24.7 us: 1.23x faster                                                        |
| sqlglot_normalize       | 147 ms                                                       | 121 ms: 1.22x faster                                                         |
| mypy2                   | 466 ms                                                       | 388 ms: 1.20x faster                                                         |
| deepcopy                | 457 us                                                       | 383 us: 1.19x faster                                                         |
| sqlglot_optimize        | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 966 us: 1.18x faster                                                         |
| genshi_xml              | 63.5 ms                                                      | 53.9 ms: 1.18x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 6.08 ms: 1.17x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.54 sec: 1.16x faster                                                       |
| json                    | 5.94 ms                                                      | 5.13 ms: 1.16x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 18.6 ms: 1.14x faster                                                        |
| sympy_expand            | 603 ms                                                       | 529 ms: 1.14x faster                                                         |
| deepcopy_reduce         | 3.91 us                                                      | 3.45 us: 1.14x faster                                                        |
| regex_dna               | 261 ms                                                       | 230 ms: 1.14x faster                                                         |
| unpack_sequence         | 59.7 ns                                                      | 52.8 ns: 1.13x faster                                                        |
| pylint                  | 562 ms                                                       | 498 ms: 1.13x faster                                                         |
| comprehensions          | 27.3 us                                                      | 24.3 us: 1.12x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.66 us: 1.11x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 85.2 ms: 1.10x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 23.6 ms: 1.10x faster                                                        |
| sympy_str               | 358 ms                                                       | 325 ms: 1.10x faster                                                         |
| async_generators        | 419 ms                                                       | 386 ms: 1.09x faster                                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.68 ms: 1.08x faster                                                        |
| sympy_sum               | 193 ms                                                       | 182 ms: 1.06x faster                                                         |
| xml_etree_parse         | 160 ms                                                       | 151 ms: 1.06x faster                                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.95 us: 1.04x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.55 us: 1.04x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 105 ms: 1.03x faster                                                         |
| python_startup          | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                                        |
| meteor_contest          | 142 ms                                                       | 138 ms: 1.03x faster                                                         |
| pickle                  | 10.1 us                                                      | 9.91 us: 1.02x faster                                                        |
| telco                   | 7.14 ms                                                      | 7.04 ms: 1.01x faster                                                        |
| pickle_dict             | 29.5 us                                                      | 30.7 us: 1.04x slower                                                        |
| unpickle                | 13.3 us                                                      | 14.2 us: 1.07x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.40 ms: 1.14x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.37 ms: 1.14x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 4.02 ms: 1.16x slower                                                        |
| dask                    | 478 ms                                                       | 563 ms: 1.18x slower                                                         |
| coverage                | 71.1 ms                                                      | 89.2 ms: 1.25x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                 |
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
