
# Results vs. 3.10.4

- fork: brandtbucher
- ref: add_small_int_new
- machine: linux-x86_64
- commit hash: 114cba6
- commit date: 2023-03-20
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                                      |
| chameleon      | 9.17 ms                                                | 6.32 ms: 1.45x faster                                                     |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                    |
| html5lib       | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                     |
| tornado_http   | 128 ms                                                 | 91.1 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 87.7 ms: 1.64x faster                                                     |
| float          | 109 ms                                                 | 73.5 ms: 1.48x faster                                                     |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                                     |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                      |
| regex_effbot   | 3.19 ms                                                | 3.50 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                                      |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                      |
| json_dumps           | 13.4 ms                                                | 9.53 ms: 1.41x faster                                                     |
| xml_etree_process    | 74.5 ms                                                | 55.3 ms: 1.35x faster                                                     |
| json_loads           | 28.7 us                                                | 24.4 us: 1.18x faster                                                     |
| xml_etree_generate   | 93.8 ms                                                | 80.8 ms: 1.16x faster                                                     |
| pickle_list          | 4.72 us                                                | 4.20 us: 1.12x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 99.1 ms: 1.12x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                      |
| unpickle             | 14.2 us                                                | 13.4 us: 1.05x faster                                                     |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                                     |
| unpickle_list        | 4.92 us                                                | 5.12 us: 1.04x slower                                                     |
| pickle_dict          | 27.6 us                                                | 31.4 us: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.89 ms: 1.58x faster                                                     |
| python_startup_no_site | 5.78 ms                                                | 6.51 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                     |
| mako            | 14.7 ms                                                | 10.1 ms: 1.46x faster                                                     |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                     |
| genshi_xml      | 63.7 ms                                                | 47.4 ms: 1.35x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.6 ms: 2.50x faster                                                     |
| deltablue               | 7.28 ms                                                | 3.15 ms: 2.31x faster                                                     |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                      |
| logging_silent          | 176 ns                                                 | 96.0 ns: 1.84x faster                                                     |
| asyncio_tcp             | 914 ms                                                 | 507 ms: 1.80x faster                                                      |
| richards                | 75.2 ms                                                | 41.8 ms: 1.80x faster                                                     |
| go                      | 226 ms                                                 | 132 ms: 1.71x faster                                                      |
| raytrace                | 467 ms                                                 | 277 ms: 1.68x faster                                                      |
| pyflate                 | 676 ms                                                 | 410 ms: 1.65x faster                                                      |
| nbody                   | 144 ms                                                 | 87.7 ms: 1.64x faster                                                     |
| scimark_monte_carlo     | 109 ms                                                 | 66.6 ms: 1.63x faster                                                     |
| chaos                   | 106 ms                                                 | 65.4 ms: 1.61x faster                                                     |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.89 ms: 1.58x faster                                                     |
| crypto_pyaes            | 117 ms                                                 | 75.0 ms: 1.56x faster                                                     |
| hexiom                  | 9.43 ms                                                | 6.09 ms: 1.55x faster                                                     |
| spectral_norm           | 150 ms                                                 | 98.1 ms: 1.52x faster                                                     |
| deepcopy_memo           | 51.7 us                                                | 33.9 us: 1.52x faster                                                     |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                      |
| float                   | 109 ms                                                 | 73.5 ms: 1.48x faster                                                     |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                     |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                      |
| mako                    | 14.7 ms                                                | 10.1 ms: 1.46x faster                                                     |
| chameleon               | 9.17 ms                                                | 6.32 ms: 1.45x faster                                                     |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                                    |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                     |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.42x faster                                                     |
| html5lib                | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                     |
| logging_simple          | 8.10 us                                                | 5.73 us: 1.41x faster                                                     |
| json_dumps              | 13.4 ms                                                | 9.53 ms: 1.41x faster                                                     |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                                     |
| tornado_http            | 128 ms                                                 | 91.1 ms: 1.41x faster                                                     |
| coroutines              | 31.6 ms                                                | 22.5 ms: 1.41x faster                                                     |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                                     |
| pprint_safe_repr        | 953 ms                                                 | 686 ms: 1.39x faster                                                      |
| scimark_fft             | 421 ms                                                 | 306 ms: 1.38x faster                                                      |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                    |
| unpack_sequence         | 59.4 ns                                                | 43.3 ns: 1.37x faster                                                     |
| async_tree_none         | 711 ms                                                 | 522 ms: 1.36x faster                                                      |
| deepcopy                | 438 us                                                 | 322 us: 1.36x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 55.3 ms: 1.35x faster                                                     |
| genshi_xml              | 63.7 ms                                                | 47.4 ms: 1.35x faster                                                     |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                                      |
| fannkuch                | 488 ms                                                 | 363 ms: 1.34x faster                                                      |
| async_tree_memoization  | 855 ms                                                 | 640 ms: 1.34x faster                                                      |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                      |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                     |
| thrift                  | 1.03 ms                                                | 777 us: 1.33x faster                                                      |
| pycparser               | 1.53 sec                                               | 1.16 sec: 1.32x faster                                                    |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 2.89 us: 1.31x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.19 ms: 1.30x faster                                                     |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                      |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                      |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 746 ms: 1.27x faster                                                      |
| nqueens                 | 100 ms                                                 | 79.1 ms: 1.26x faster                                                     |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                    |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.6 ms: 1.22x faster                                                     |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                      |
| dulwich_log             | 75.8 ms                                                | 63.0 ms: 1.20x faster                                                     |
| bench_thread_pool       | 946 us                                                 | 788 us: 1.20x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                     |
| json_loads              | 28.7 us                                                | 24.4 us: 1.18x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                                     |
| xml_etree_generate      | 93.8 ms                                                | 80.8 ms: 1.16x faster                                                     |
| sympy_expand            | 534 ms                                                 | 461 ms: 1.16x faster                                                      |
| json                    | 5.35 ms                                                | 4.63 ms: 1.16x faster                                                     |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                                      |
| djangocms               | 36.9 us                                                | 32.2 us: 1.15x faster                                                     |
| pickle_list             | 4.72 us                                                | 4.20 us: 1.12x faster                                                     |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 99.1 ms: 1.12x faster                                                     |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.11x faster                                                      |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.49 ms: 1.10x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.51 sec: 1.09x faster                                                    |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                     |
| unpickle                | 14.2 us                                                | 13.4 us: 1.05x faster                                                     |
| telco                   | 6.73 ms                                                | 6.49 ms: 1.04x faster                                                     |
| async_generators        | 426 ms                                                 | 413 ms: 1.03x faster                                                      |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                      |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                                     |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                                      |
| unpickle_list           | 4.92 us                                                | 5.12 us: 1.04x slower                                                     |
| regex_effbot            | 3.19 ms                                                | 3.50 ms: 1.09x slower                                                     |
| gc_traversal            | 3.53 ms                                                | 3.93 ms: 1.12x slower                                                     |
| python_startup_no_site  | 5.78 ms                                                | 6.51 ms: 1.13x slower                                                     |
| pickle_dict             | 27.6 us                                                | 31.4 us: 1.14x slower                                                     |
| dask                    | 436 ms                                                 | 503 ms: 1.15x slower                                                      |
| coverage                | 74.7 ms                                                | 95.1 ms: 1.27x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230320-3.12.0a6+-114cba6/bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6.json: comprehensions
