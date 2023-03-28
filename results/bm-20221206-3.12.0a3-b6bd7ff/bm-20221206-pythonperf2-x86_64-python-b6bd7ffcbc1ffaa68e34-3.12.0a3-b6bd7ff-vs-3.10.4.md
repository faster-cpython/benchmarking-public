
# Results vs. 3.10.4

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: linux-x86_64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 280 ms: 1.26x faster                                                        |
| chameleon      | 9.62 ms                                                      | 7.70 ms: 1.25x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.79 sec: 1.22x faster                                                      |
| html5lib       | 96.3 ms                                                      | 67.0 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 74.6 ms: 1.47x faster                                                       |
| nbody          | 132 ms                                                       | 92.2 ms: 1.43x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 148 ms: 1.29x faster                                                        |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 23.7 ms: 1.10x faster                                                       |
| regex_effbot   | 2.99 ms                                                      | 3.51 ms: 1.18x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 214 us: 1.49x faster                                                        |
| pickle_pure_python   | 451 us                                                       | 313 us: 1.44x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 55.2 ms: 1.41x faster                                                       |
| json_dumps           | 14.3 ms                                                      | 10.5 ms: 1.36x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.2 us: 1.25x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 79.2 ms: 1.19x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.12x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.44 us: 1.07x faster                                                       |
| pickle_list          | 4.11 us                                                      | 3.94 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 107 ms: 1.02x faster                                                        |
| pickle               | 10.1 us                                                      | 10.0 us: 1.01x faster                                                       |
| unpickle             | 13.3 us                                                      | 13.7 us: 1.03x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 31.2 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.16x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.9 ms: 1.06x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.92 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| django_template | 52.0 ms                                                      | 40.0 ms: 1.30x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 25.1 ms: 1.26x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 53.0 ms: 1.20x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.69 ms: 2.05x faster                                                       |
| logging_silent          | 165 ns                                                       | 99.6 ns: 1.65x faster                                                       |
| pyflate                 | 731 ms                                                       | 443 ms: 1.65x faster                                                        |
| go                      | 264 ms                                                       | 164 ms: 1.61x faster                                                        |
| scimark_lu              | 164 ms                                                       | 102 ms: 1.60x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 67.9 ms: 1.60x faster                                                       |
| scimark_sor             | 177 ms                                                       | 111 ms: 1.60x faster                                                        |
| richards                | 73.9 ms                                                      | 46.2 ms: 1.60x faster                                                       |
| bench_mp_pool           | 7.10 ms                                                      | 4.56 ms: 1.56x faster                                                       |
| raytrace                | 491 ms                                                       | 316 ms: 1.56x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 214 us: 1.49x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.52 ms: 1.48x faster                                                       |
| float                   | 109 ms                                                       | 74.6 ms: 1.47x faster                                                       |
| pickle_pure_python      | 451 us                                                       | 313 us: 1.44x faster                                                        |
| html5lib                | 96.3 ms                                                      | 67.0 ms: 1.44x faster                                                       |
| nbody                   | 132 ms                                                       | 92.2 ms: 1.43x faster                                                       |
| sqlglot_transpile       | 2.69 ms                                                      | 1.88 ms: 1.43x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 83.2 ms: 1.42x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 6.75 ms: 1.41x faster                                                       |
| spectral_norm           | 138 ms                                                       | 98.0 ms: 1.41x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 55.2 ms: 1.41x faster                                                       |
| chaos                   | 108 ms                                                       | 77.8 ms: 1.39x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.71 ms: 1.37x faster                                                       |
| json_dumps              | 14.3 ms                                                      | 10.5 ms: 1.36x faster                                                       |
| pprint_pformat          | 2.12 sec                                                     | 1.57 sec: 1.35x faster                                                      |
| async_tree_io           | 1.61 sec                                                     | 1.19 sec: 1.35x faster                                                      |
| pprint_safe_repr        | 1.03 sec                                                     | 760 ms: 1.35x faster                                                        |
| thrift                  | 1.23 ms                                                      | 912 us: 1.34x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 36.9 us: 1.33x faster                                                       |
| async_tree_none         | 698 ms                                                       | 530 ms: 1.32x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 45.3 ns: 1.32x faster                                                       |
| async_tree_memoization  | 822 ms                                                       | 624 ms: 1.32x faster                                                        |
| logging_simple          | 9.24 us                                                      | 7.02 us: 1.32x faster                                                       |
| logging_format          | 9.94 us                                                      | 7.63 us: 1.30x faster                                                       |
| django_template         | 52.0 ms                                                      | 40.0 ms: 1.30x faster                                                       |
| scimark_fft             | 359 ms                                                       | 278 ms: 1.29x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.28 sec: 1.29x faster                                                      |
| regex_compile           | 191 ms                                                       | 148 ms: 1.29x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 25.1 ms: 1.26x faster                                                       |
| 2to3                    | 352 ms                                                       | 280 ms: 1.26x faster                                                        |
| async_generators        | 419 ms                                                       | 334 ms: 1.25x faster                                                        |
| json_loads              | 30.3 us                                                      | 24.2 us: 1.25x faster                                                       |
| chameleon               | 9.62 ms                                                      | 7.70 ms: 1.25x faster                                                       |
| mypy2                   | 466 ms                                                       | 375 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 770 ms: 1.24x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.79 sec: 1.22x faster                                                      |
| sqlglot_normalize       | 147 ms                                                       | 122 ms: 1.21x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 66.6 ms: 1.21x faster                                                       |
| genshi_xml              | 63.5 ms                                                      | 53.0 ms: 1.20x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 58.5 ms: 1.20x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 79.2 ms: 1.19x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 968 us: 1.18x faster                                                        |
| deepcopy                | 457 us                                                       | 390 us: 1.17x faster                                                        |
| json                    | 5.94 ms                                                      | 5.10 ms: 1.16x faster                                                       |
| dask                    | 478 ms                                                       | 412 ms: 1.16x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.56 us: 1.16x faster                                                       |
| create_gc_cycles        | 1.80 ms                                                      | 1.59 ms: 1.13x faster                                                       |
| xml_etree_parse         | 160 ms                                                       | 142 ms: 1.12x faster                                                        |
| regex_dna               | 261 ms                                                       | 233 ms: 1.12x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.49 us: 1.12x faster                                                       |
| fannkuch                | 496 ms                                                       | 443 ms: 1.12x faster                                                        |
| sympy_expand            | 603 ms                                                       | 542 ms: 1.11x faster                                                        |
| nqueens                 | 114 ms                                                       | 102 ms: 1.11x faster                                                        |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 23.7 ms: 1.10x faster                                                       |
| pathlib                 | 21.3 ms                                                      | 19.4 ms: 1.10x faster                                                       |
| coroutines              | 30.6 ms                                                      | 28.0 ms: 1.09x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.7 ms: 1.09x faster                                                       |
| mdp                     | 2.95 sec                                                     | 2.71 sec: 1.09x faster                                                      |
| pidigits                | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| sympy_str               | 358 ms                                                       | 335 ms: 1.07x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.44 us: 1.07x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.73 ms: 1.06x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.9 ms: 1.06x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 749 ms: 1.05x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.94 us: 1.04x faster                                                       |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 107 ms: 1.02x faster                                                        |
| pickle                  | 10.1 us                                                      | 10.0 us: 1.01x faster                                                       |
| comprehensions          | 27.3 us                                                      | 27.1 us: 1.01x faster                                                       |
| unpickle                | 13.3 us                                                      | 13.7 us: 1.03x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 31.2 us: 1.06x slower                                                       |
| generators              | 57.0 ms                                                      | 60.6 ms: 1.06x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.92 ms: 1.08x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 4.01 ms: 1.16x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.51 ms: 1.18x slower                                                       |
| coverage                | 71.1 ms                                                      | 90.9 ms: 1.28x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.24x faster                                                                |
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
