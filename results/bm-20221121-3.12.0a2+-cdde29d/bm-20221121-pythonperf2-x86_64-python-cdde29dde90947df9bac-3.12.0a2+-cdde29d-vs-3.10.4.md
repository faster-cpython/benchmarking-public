
# Results vs. 3.10.4

- fork: python
- ref: cdde29dde90947df9bac
- machine: linux-x86_64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 280 ms: 1.26x faster                                                         |
| chameleon      | 9.62 ms                                                      | 7.42 ms: 1.30x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                                       |
| html5lib       | 96.3 ms                                                      | 67.3 ms: 1.43x faster                                                        |
| tornado_http   | 151 ms                                                       | 121 ms: 1.25x faster                                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.6 ms: 1.49x faster                                                        |
| nbody          | 132 ms                                                       | 93.5 ms: 1.41x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 150 ms: 1.28x faster                                                         |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 23.7 ms: 1.10x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 208 us: 1.53x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 315 us: 1.43x faster                                                         |
| xml_etree_process    | 77.6 ms                                                      | 55.2 ms: 1.40x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 10.4 ms: 1.38x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.3 us: 1.25x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 79.5 ms: 1.18x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                         |
| xml_etree_iterparse  | 109 ms                                                       | 102 ms: 1.07x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.88 us: 1.06x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.59 us: 1.03x faster                                                        |
| pickle               | 10.1 us                                                      | 9.96 us: 1.02x faster                                                        |
| unpickle             | 13.3 us                                                      | 13.4 us: 1.01x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 32.3 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| django_template | 52.0 ms                                                      | 41.0 ms: 1.27x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 26.3 ms: 1.20x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 55.4 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.67 ms: 2.05x faster                                                        |
| go                      | 264 ms                                                       | 159 ms: 1.66x faster                                                         |
| logging_silent          | 165 ns                                                       | 99.6 ns: 1.65x faster                                                        |
| raytrace                | 491 ms                                                       | 299 ms: 1.64x faster                                                         |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.63x faster                                                         |
| pyflate                 | 731 ms                                                       | 450 ms: 1.62x faster                                                         |
| bench_mp_pool           | 7.10 ms                                                      | 4.42 ms: 1.61x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 68.5 ms: 1.59x faster                                                        |
| richards                | 73.9 ms                                                      | 47.6 ms: 1.55x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 208 us: 1.53x faster                                                         |
| float                   | 109 ms                                                       | 73.6 ms: 1.49x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.53 ms: 1.47x faster                                                        |
| spectral_norm           | 138 ms                                                       | 94.6 ms: 1.46x faster                                                        |
| scimark_lu              | 164 ms                                                       | 114 ms: 1.44x faster                                                         |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 315 us: 1.43x faster                                                         |
| chaos                   | 108 ms                                                       | 75.3 ms: 1.43x faster                                                        |
| html5lib                | 96.3 ms                                                      | 67.3 ms: 1.43x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.89 ms: 1.42x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 83.6 ms: 1.42x faster                                                        |
| nbody                   | 132 ms                                                       | 93.5 ms: 1.41x faster                                                        |
| xml_etree_process       | 77.6 ms                                                      | 55.2 ms: 1.40x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.65 ms: 1.40x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                       |
| thrift                  | 1.23 ms                                                      | 880 us: 1.39x faster                                                         |
| json_dumps              | 14.3 ms                                                      | 10.4 ms: 1.38x faster                                                        |
| async_tree_none         | 698 ms                                                       | 515 ms: 1.36x faster                                                         |
| hexiom                  | 9.54 ms                                                      | 7.08 ms: 1.35x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 36.6 us: 1.34x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 614 ms: 1.34x faster                                                         |
| unpack_sequence         | 59.7 ns                                                      | 45.5 ns: 1.31x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.62 sec: 1.31x faster                                                       |
| aiohttp                 | 1.18 ms                                                      | 898 us: 1.31x faster                                                         |
| logging_simple          | 9.24 us                                                      | 7.08 us: 1.30x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 788 ms: 1.30x faster                                                         |
| logging_format          | 9.94 us                                                      | 7.65 us: 1.30x faster                                                        |
| chameleon               | 9.62 ms                                                      | 7.42 ms: 1.30x faster                                                        |
| gunicorn                | 1.15 ms                                                      | 889 us: 1.29x faster                                                         |
| regex_compile           | 191 ms                                                       | 150 ms: 1.28x faster                                                         |
| scimark_fft             | 359 ms                                                       | 282 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed | 951 ms                                                       | 748 ms: 1.27x faster                                                         |
| django_template         | 52.0 ms                                                      | 41.0 ms: 1.27x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.32 sec: 1.26x faster                                                       |
| 2to3                    | 352 ms                                                       | 280 ms: 1.26x faster                                                         |
| async_generators        | 419 ms                                                       | 333 ms: 1.26x faster                                                         |
| mypy2                   | 466 ms                                                       | 374 ms: 1.25x faster                                                         |
| tornado_http            | 151 ms                                                       | 121 ms: 1.25x faster                                                         |
| json_loads              | 30.3 us                                                      | 24.3 us: 1.25x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                                       |
| sqlglot_normalize       | 147 ms                                                       | 122 ms: 1.21x faster                                                         |
| genshi_text             | 31.7 ms                                                      | 26.3 ms: 1.20x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 58.5 ms: 1.20x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 67.4 ms: 1.19x faster                                                        |
| fannkuch                | 496 ms                                                       | 416 ms: 1.19x faster                                                         |
| bench_thread_pool       | 1.14 ms                                                      | 957 us: 1.19x faster                                                         |
| xml_etree_generate      | 94.1 ms                                                      | 79.5 ms: 1.18x faster                                                        |
| deepcopy                | 457 us                                                       | 388 us: 1.18x faster                                                         |
| json                    | 5.94 ms                                                      | 5.07 ms: 1.17x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.35 us: 1.17x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 138 ms: 1.16x faster                                                         |
| sqlite_synth            | 2.96 us                                                      | 2.56 us: 1.16x faster                                                        |
| dask                    | 478 ms                                                       | 416 ms: 1.15x faster                                                         |
| regex_dna               | 261 ms                                                       | 227 ms: 1.15x faster                                                         |
| genshi_xml              | 63.5 ms                                                      | 55.4 ms: 1.15x faster                                                        |
| nqueens                 | 114 ms                                                       | 99.6 ms: 1.14x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.59 ms: 1.13x faster                                                        |
| meteor_contest          | 142 ms                                                       | 127 ms: 1.11x faster                                                         |
| coroutines              | 30.6 ms                                                      | 27.6 ms: 1.11x faster                                                        |
| sympy_expand            | 603 ms                                                       | 547 ms: 1.10x faster                                                         |
| pathlib                 | 21.3 ms                                                      | 19.3 ms: 1.10x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 23.7 ms: 1.10x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.6 ms: 1.10x faster                                                        |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| xml_etree_iterparse     | 109 ms                                                       | 102 ms: 1.07x faster                                                         |
| sympy_str               | 358 ms                                                       | 335 ms: 1.07x faster                                                         |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.78 sec: 1.06x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.74 ms: 1.06x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.88 us: 1.06x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 744 ms: 1.06x faster                                                         |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                                         |
| unpickle_list           | 4.73 us                                                      | 4.59 us: 1.03x faster                                                        |
| pickle                  | 10.1 us                                                      | 9.96 us: 1.02x faster                                                        |
| unpickle                | 13.3 us                                                      | 13.4 us: 1.01x slower                                                        |
| comprehensions          | 27.3 us                                                      | 27.5 us: 1.01x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.61 ms: 1.04x slower                                                        |
| generators              | 57.0 ms                                                      | 60.8 ms: 1.07x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 32.3 us: 1.09x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                                        |
| coverage                | 71.1 ms                                                      | 86.9 ms: 1.22x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.24x faster                                                                 |
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
