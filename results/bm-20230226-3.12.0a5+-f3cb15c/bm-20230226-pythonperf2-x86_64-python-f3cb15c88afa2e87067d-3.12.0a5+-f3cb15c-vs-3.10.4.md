
# Results vs. 3.10.4

- fork: python
- ref: f3cb15c88afa2e87067d
- machine: linux-x86_64
- commit hash: f3cb15c
- commit date: 2023-02-26
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 285 ms: 1.23x faster                                                         |
| chameleon      | 9.62 ms                                                      | 6.83 ms: 1.41x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.82 sec: 1.21x faster                                                       |
| html5lib       | 96.3 ms                                                      | 67.1 ms: 1.43x faster                                                        |
| tornado_http   | 151 ms                                                       | 117 ms: 1.29x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 72.5 ms: 1.51x faster                                                        |
| nbody          | 132 ms                                                       | 94.5 ms: 1.40x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 147 ms: 1.30x faster                                                         |
| regex_dna      | 261 ms                                                       | 222 ms: 1.18x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 22.9 ms: 1.14x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.31 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 205 us: 1.55x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 310 us: 1.46x faster                                                         |
| json_dumps           | 14.3 ms                                                      | 10.1 ms: 1.42x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 58.2 ms: 1.33x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.1 us: 1.26x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 84.2 ms: 1.12x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                         |
| unpickle_list        | 4.73 us                                                      | 4.43 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 103 ms: 1.06x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.92 us: 1.05x faster                                                        |
| pickle               | 10.1 us                                                      | 9.80 us: 1.03x faster                                                        |
| unpickle             | 13.3 us                                                      | 13.2 us: 1.01x faster                                                        |
| pickle_dict          | 29.5 us                                                      | 31.3 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.39 ms: 1.14x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.87 ms: 1.49x faster                                                        |
| django_template | 52.0 ms                                                      | 41.1 ms: 1.26x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 25.1 ms: 1.26x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 55.8 ms: 1.14x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.35 ms: 2.25x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 387 ms: 2.03x faster                                                         |
| go                      | 264 ms                                                       | 150 ms: 1.76x faster                                                         |
| logging_silent          | 165 ns                                                       | 95.3 ns: 1.73x faster                                                        |
| pyflate                 | 731 ms                                                       | 434 ms: 1.69x faster                                                         |
| raytrace                | 491 ms                                                       | 298 ms: 1.65x faster                                                         |
| scimark_sor             | 177 ms                                                       | 108 ms: 1.64x faster                                                         |
| richards                | 73.9 ms                                                      | 46.4 ms: 1.59x faster                                                        |
| scimark_lu              | 164 ms                                                       | 104 ms: 1.58x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 69.4 ms: 1.57x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 205 us: 1.55x faster                                                         |
| chaos                   | 108 ms                                                       | 71.0 ms: 1.52x faster                                                        |
| float                   | 109 ms                                                       | 72.5 ms: 1.51x faster                                                        |
| mako                    | 14.7 ms                                                      | 9.87 ms: 1.49x faster                                                        |
| generators              | 57.0 ms                                                      | 38.6 ms: 1.48x faster                                                        |
| hexiom                  | 9.54 ms                                                      | 6.53 ms: 1.46x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 310 us: 1.46x faster                                                         |
| html5lib                | 96.3 ms                                                      | 67.1 ms: 1.43x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.96 ms: 1.43x faster                                                        |
| spectral_norm           | 138 ms                                                       | 96.4 ms: 1.43x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.1 ms: 1.42x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.58 ms: 1.42x faster                                                        |
| chameleon               | 9.62 ms                                                      | 6.83 ms: 1.41x faster                                                        |
| nbody                   | 132 ms                                                       | 94.5 ms: 1.40x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 84.8 ms: 1.40x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.95 ms: 1.38x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.18 sec: 1.37x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 759 ms: 1.35x faster                                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.57 sec: 1.35x faster                                                       |
| deepcopy_memo           | 49.2 us                                                      | 36.6 us: 1.35x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 615 ms: 1.34x faster                                                         |
| async_tree_none         | 698 ms                                                       | 524 ms: 1.33x faster                                                         |
| xml_etree_process       | 77.6 ms                                                      | 58.2 ms: 1.33x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 45.0 ns: 1.33x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.27 sec: 1.30x faster                                                       |
| logging_simple          | 9.24 us                                                      | 7.11 us: 1.30x faster                                                        |
| thrift                  | 1.23 ms                                                      | 945 us: 1.30x faster                                                         |
| regex_compile           | 191 ms                                                       | 147 ms: 1.30x faster                                                         |
| tornado_http            | 151 ms                                                       | 117 ms: 1.29x faster                                                         |
| scimark_fft             | 359 ms                                                       | 281 ms: 1.28x faster                                                         |
| django_template         | 52.0 ms                                                      | 41.1 ms: 1.26x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 25.1 ms: 1.26x faster                                                        |
| logging_format          | 9.94 us                                                      | 7.89 us: 1.26x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 756 ms: 1.26x faster                                                         |
| json_loads              | 30.3 us                                                      | 24.1 us: 1.26x faster                                                        |
| coroutines              | 30.6 ms                                                      | 24.4 ms: 1.25x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 65.0 ms: 1.24x faster                                                        |
| 2to3                    | 352 ms                                                       | 285 ms: 1.23x faster                                                         |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.13 ms: 1.23x faster                                                        |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.23x faster                                                         |
| fannkuch                | 496 ms                                                       | 404 ms: 1.23x faster                                                         |
| mypy2                   | 466 ms                                                       | 381 ms: 1.22x faster                                                         |
| docutils                | 3.41 sec                                                     | 2.82 sec: 1.21x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 58.2 ms: 1.21x faster                                                        |
| json                    | 5.94 ms                                                      | 4.98 ms: 1.19x faster                                                        |
| regex_dna               | 261 ms                                                       | 222 ms: 1.18x faster                                                         |
| bench_thread_pool       | 1.14 ms                                                      | 985 us: 1.16x faster                                                         |
| sqlite_synth            | 2.96 us                                                      | 2.57 us: 1.15x faster                                                        |
| deepcopy                | 457 us                                                       | 398 us: 1.15x faster                                                         |
| nqueens                 | 114 ms                                                       | 99.1 ms: 1.15x faster                                                        |
| genshi_xml              | 63.5 ms                                                      | 55.8 ms: 1.14x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 22.9 ms: 1.14x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 18.8 ms: 1.13x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.47 us: 1.13x faster                                                        |
| meteor_contest          | 142 ms                                                       | 126 ms: 1.13x faster                                                         |
| xml_etree_generate      | 94.1 ms                                                      | 84.2 ms: 1.12x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 144 ms: 1.11x faster                                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.4 ms: 1.11x faster                                                        |
| sympy_expand            | 603 ms                                                       | 546 ms: 1.10x faster                                                         |
| mdp                     | 2.95 sec                                                     | 2.71 sec: 1.09x faster                                                       |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.68 ms: 1.08x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.43 us: 1.07x faster                                                        |
| sympy_str               | 358 ms                                                       | 336 ms: 1.07x faster                                                         |
| async_generators        | 419 ms                                                       | 393 ms: 1.06x faster                                                         |
| xml_etree_iterparse     | 109 ms                                                       | 103 ms: 1.06x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.92 us: 1.05x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.83 ms: 1.04x faster                                                        |
| pickle                  | 10.1 us                                                      | 9.80 us: 1.03x faster                                                        |
| sympy_sum               | 193 ms                                                       | 188 ms: 1.02x faster                                                         |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                        |
| unpickle                | 13.3 us                                                      | 13.2 us: 1.01x faster                                                        |
| comprehensions          | 27.3 us                                                      | 27.4 us: 1.01x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 31.3 us: 1.06x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.31 ms: 1.11x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.39 ms: 1.14x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.99 ms: 1.15x slower                                                        |
| dask                    | 478 ms                                                       | 563 ms: 1.18x slower                                                         |
| coverage                | 71.1 ms                                                      | 85.2 ms: 1.20x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                 |
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
