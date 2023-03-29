
# Results vs. 3.10.4

- fork: python
- ref: 3c67ec394faac79d2608
- machine: linux-x86_64
- commit hash: 3c67ec3
- commit date: 2023-02-07
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 282 ms: 1.25x faster                                                        |
| chameleon      | 9.62 ms                                                      | 7.46 ms: 1.29x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                                      |
| html5lib       | 96.3 ms                                                      | 65.3 ms: 1.48x faster                                                       |
| tornado_http   | 151 ms                                                       | 117 ms: 1.29x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 71.9 ms: 1.52x faster                                                       |
| nbody          | 132 ms                                                       | 101 ms: 1.31x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 145 ms: 1.32x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 22.7 ms: 1.15x faster                                                       |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 204 us: 1.56x faster                                                        |
| pickle_pure_python   | 451 us                                                       | 312 us: 1.45x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 10.0 ms: 1.42x faster                                                       |
| xml_etree_process    | 77.6 ms                                                      | 55.6 ms: 1.39x faster                                                       |
| json_loads           | 30.3 us                                                      | 23.8 us: 1.27x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 80.6 ms: 1.17x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.84 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 103 ms: 1.06x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.50 us: 1.05x faster                                                       |
| unpickle             | 13.3 us                                                      | 12.8 us: 1.04x faster                                                       |
| pickle               | 10.1 us                                                      | 9.88 us: 1.03x faster                                                       |
| pickle_dict          | 29.5 us                                                      | 31.6 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.25 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.44x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 24.6 ms: 1.29x faster                                                       |
| django_template | 52.0 ms                                                      | 40.5 ms: 1.28x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 53.4 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.60 ms: 2.10x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 388 ms: 2.03x faster                                                        |
| go                      | 264 ms                                                       | 152 ms: 1.73x faster                                                        |
| pyflate                 | 731 ms                                                       | 428 ms: 1.71x faster                                                        |
| logging_silent          | 165 ns                                                       | 96.5 ns: 1.70x faster                                                       |
| scimark_sor             | 177 ms                                                       | 105 ms: 1.69x faster                                                        |
| raytrace                | 491 ms                                                       | 301 ms: 1.63x faster                                                        |
| richards                | 73.9 ms                                                      | 46.1 ms: 1.60x faster                                                       |
| scimark_lu              | 164 ms                                                       | 104 ms: 1.58x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 204 us: 1.56x faster                                                        |
| chaos                   | 108 ms                                                       | 69.6 ms: 1.55x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                       | 70.2 ms: 1.55x faster                                                       |
| float                   | 109 ms                                                       | 71.9 ms: 1.52x faster                                                       |
| bench_mp_pool           | 7.10 ms                                                      | 4.71 ms: 1.51x faster                                                       |
| html5lib                | 96.3 ms                                                      | 65.3 ms: 1.48x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 6.49 ms: 1.47x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 81.8 ms: 1.45x faster                                                       |
| pickle_pure_python      | 451 us                                                       | 312 us: 1.45x faster                                                        |
| spectral_norm           | 138 ms                                                       | 95.4 ms: 1.44x faster                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 1.56 ms: 1.44x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.3 ms: 1.44x faster                                                       |
| json_dumps              | 14.3 ms                                                      | 10.0 ms: 1.42x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.61 ms: 1.41x faster                                                       |
| sqlglot_transpile       | 2.69 ms                                                      | 1.93 ms: 1.39x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 55.6 ms: 1.39x faster                                                       |
| async_tree_none         | 698 ms                                                       | 503 ms: 1.39x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.53 sec: 1.39x faster                                                      |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                      |
| logging_simple          | 9.24 us                                                      | 6.67 us: 1.38x faster                                                       |
| unpack_sequence         | 59.7 ns                                                      | 43.3 ns: 1.38x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 744 ms: 1.38x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 35.8 us: 1.37x faster                                                       |
| async_tree_memoization  | 822 ms                                                       | 601 ms: 1.37x faster                                                        |
| logging_format          | 9.94 us                                                      | 7.43 us: 1.34x faster                                                       |
| regex_compile           | 191 ms                                                       | 145 ms: 1.32x faster                                                        |
| thrift                  | 1.23 ms                                                      | 935 us: 1.31x faster                                                        |
| nbody                   | 132 ms                                                       | 101 ms: 1.31x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.28 sec: 1.30x faster                                                      |
| async_tree_cpu_io_mixed | 951 ms                                                       | 737 ms: 1.29x faster                                                        |
| tornado_http            | 151 ms                                                       | 117 ms: 1.29x faster                                                        |
| scimark_fft             | 359 ms                                                       | 278 ms: 1.29x faster                                                        |
| chameleon               | 9.62 ms                                                      | 7.46 ms: 1.29x faster                                                       |
| async_generators        | 419 ms                                                       | 325 ms: 1.29x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 24.6 ms: 1.29x faster                                                       |
| django_template         | 52.0 ms                                                      | 40.5 ms: 1.28x faster                                                       |
| comprehensions          | 27.3 us                                                      | 21.3 us: 1.28x faster                                                       |
| json_loads              | 30.3 us                                                      | 23.8 us: 1.27x faster                                                       |
| 2to3                    | 352 ms                                                       | 282 ms: 1.25x faster                                                        |
| mypy2                   | 466 ms                                                       | 379 ms: 1.23x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                                      |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.22x faster                                                        |
| fannkuch                | 496 ms                                                       | 409 ms: 1.21x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 57.7 ms: 1.21x faster                                                       |
| dulwich_log             | 80.5 ms                                                      | 66.6 ms: 1.21x faster                                                       |
| nqueens                 | 114 ms                                                       | 94.2 ms: 1.21x faster                                                       |
| json                    | 5.94 ms                                                      | 4.94 ms: 1.20x faster                                                       |
| deepcopy                | 457 us                                                       | 383 us: 1.19x faster                                                        |
| genshi_xml              | 63.5 ms                                                      | 53.4 ms: 1.19x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.30 us: 1.19x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 971 us: 1.17x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 80.6 ms: 1.17x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 24.3 ms: 1.16x faster                                                       |
| sqlite_synth            | 2.96 us                                                      | 2.58 us: 1.15x faster                                                       |
| sympy_expand            | 603 ms                                                       | 526 ms: 1.15x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 22.7 ms: 1.15x faster                                                       |
| sympy_str               | 358 ms                                                       | 313 ms: 1.14x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| sympy_sum               | 193 ms                                                       | 172 ms: 1.12x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 19.1 ms: 1.11x faster                                                       |
| mdp                     | 2.95 sec                                                     | 2.66 sec: 1.11x faster                                                      |
| meteor_contest          | 142 ms                                                       | 128 ms: 1.11x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.64 ms: 1.10x faster                                                       |
| regex_dna               | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.59 ms: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.84 us: 1.07x faster                                                       |
| xml_etree_iterparse     | 109 ms                                                       | 103 ms: 1.06x faster                                                        |
| coroutines              | 30.6 ms                                                      | 29.1 ms: 1.05x faster                                                       |
| unpickle_list           | 4.73 us                                                      | 4.50 us: 1.05x faster                                                       |
| unpickle                | 13.3 us                                                      | 12.8 us: 1.04x faster                                                       |
| pickle                  | 10.1 us                                                      | 9.88 us: 1.03x faster                                                       |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.55 ms: 1.03x slower                                                       |
| generators              | 57.0 ms                                                      | 60.4 ms: 1.06x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 31.6 us: 1.07x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 8.25 ms: 1.13x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                                       |
| dask                    | 478 ms                                                       | 562 ms: 1.18x slower                                                        |
| coverage                | 71.1 ms                                                      | 86.0 ms: 1.21x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                                |
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
