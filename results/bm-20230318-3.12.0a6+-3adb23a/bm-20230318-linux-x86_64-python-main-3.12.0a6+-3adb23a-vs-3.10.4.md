
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3adb23a
- commit date: 2023-03-18
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.35 ms: 1.44x faster                                  |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.25x faster                                 |
| html5lib       | 85.9 ms                                                | 61.2 ms: 1.40x faster                                  |
| tornado_http   | 128 ms                                                 | 91.2 ms: 1.41x faster                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 86.0 ms: 1.67x faster                                  |
| float          | 109 ms                                                 | 73.9 ms: 1.47x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.32x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                  |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.63 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.57 ms: 1.40x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 55.2 ms: 1.35x faster                                  |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.4 ms: 1.17x faster                                  |
| pickle_list          | 4.72 us                                                | 4.26 us: 1.11x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.2 us                                                | 13.5 us: 1.05x faster                                  |
| unpickle_list        | 4.92 us                                                | 5.00 us: 1.01x slower                                  |
| pickle               | 10.2 us                                                | 10.4 us: 1.03x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.3 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.91 ms: 1.58x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.52 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.1 ms: 1.46x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.0 ms: 1.46x faster                                  |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                  |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.3 ms: 2.60x faster                                  |
| deltablue               | 7.28 ms                                                | 3.17 ms: 2.30x faster                                  |
| logging_silent          | 176 ns                                                 | 94.9 ns: 1.86x faster                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                   |
| asyncio_tcp             | 914 ms                                                 | 507 ms: 1.80x faster                                   |
| richards                | 75.2 ms                                                | 41.9 ms: 1.80x faster                                  |
| nbody                   | 144 ms                                                 | 86.0 ms: 1.67x faster                                  |
| raytrace                | 467 ms                                                 | 280 ms: 1.66x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.7 ms: 1.65x faster                                  |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                   |
| pyflate                 | 676 ms                                                 | 414 ms: 1.63x faster                                   |
| spectral_norm           | 150 ms                                                 | 92.7 ms: 1.61x faster                                  |
| chaos                   | 106 ms                                                 | 66.0 ms: 1.60x faster                                  |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                   |
| crypto_pyaes            | 117 ms                                                 | 73.7 ms: 1.58x faster                                  |
| python_startup          | 14.1 ms                                                | 8.91 ms: 1.58x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.11 ms: 1.54x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                   |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                  |
| float                   | 109 ms                                                 | 73.9 ms: 1.47x faster                                  |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.47x faster                                   |
| mako                    | 14.7 ms                                                | 10.1 ms: 1.46x faster                                  |
| genshi_text             | 30.6 ms                                                | 21.0 ms: 1.46x faster                                  |
| chameleon               | 9.17 ms                                                | 6.35 ms: 1.44x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                  |
| logging_simple          | 8.10 us                                                | 5.69 us: 1.42x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                 |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                  |
| tornado_http            | 128 ms                                                 | 91.2 ms: 1.41x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.57 ms: 1.40x faster                                  |
| logging_format          | 8.85 us                                                | 6.31 us: 1.40x faster                                  |
| html5lib                | 85.9 ms                                                | 61.2 ms: 1.40x faster                                  |
| scimark_fft             | 421 ms                                                 | 300 ms: 1.40x faster                                   |
| coroutines              | 31.6 ms                                                | 22.8 ms: 1.39x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 686 ms: 1.39x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                 |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.37x faster                                 |
| unpack_sequence         | 59.4 ns                                                | 43.2 ns: 1.37x faster                                  |
| async_tree_none         | 711 ms                                                 | 523 ms: 1.36x faster                                   |
| deepcopy                | 438 us                                                 | 323 us: 1.35x faster                                   |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 55.2 ms: 1.35x faster                                  |
| 2to3                    | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| thrift                  | 1.03 ms                                                | 771 us: 1.34x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 644 ms: 1.33x faster                                   |
| regex_compile           | 177 ms                                                 | 135 ms: 1.32x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.32x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.31x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.30x faster                                   |
| mypy2                   | 430 ms                                                 | 332 ms: 1.30x faster                                   |
| fannkuch                | 488 ms                                                 | 377 ms: 1.30x faster                                   |
| nqueens                 | 100 ms                                                 | 77.9 ms: 1.28x faster                                  |
| sqlglot_optimize        | 65.2 ms                                                | 50.9 ms: 1.28x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 747 ms: 1.27x faster                                   |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.25x faster                                 |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                   |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.8 ms: 1.21x faster                                  |
| bench_thread_pool       | 946 us                                                 | 785 us: 1.21x faster                                   |
| dulwich_log             | 75.8 ms                                                | 63.0 ms: 1.20x faster                                  |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 80.4 ms: 1.17x faster                                  |
| sympy_expand            | 534 ms                                                 | 458 ms: 1.17x faster                                   |
| json                    | 5.35 ms                                                | 4.62 ms: 1.16x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                  |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| djangocms               | 36.9 us                                                | 32.7 us: 1.13x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                  |
| pickle_list             | 4.72 us                                                | 4.26 us: 1.11x faster                                  |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                   |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                   |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                   |
| mdp                     | 2.74 sec                                               | 2.61 sec: 1.05x faster                                 |
| telco                   | 6.73 ms                                                | 6.43 ms: 1.05x faster                                  |
| unpickle                | 14.2 us                                                | 13.5 us: 1.05x faster                                  |
| async_generators        | 426 ms                                                 | 413 ms: 1.03x faster                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| unpickle_list           | 4.92 us                                                | 5.00 us: 1.01x slower                                  |
| pickle                  | 10.2 us                                                | 10.4 us: 1.03x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.90 ms: 1.11x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.52 ms: 1.13x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.3 us: 1.13x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.63 ms: 1.14x slower                                  |
| dask                    | 436 ms                                                 | 501 ms: 1.15x slower                                   |
| coverage                | 74.7 ms                                                | 97.0 ms: 1.30x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230318-3.12.0a6+-3adb23a/bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a.json: comprehensions
