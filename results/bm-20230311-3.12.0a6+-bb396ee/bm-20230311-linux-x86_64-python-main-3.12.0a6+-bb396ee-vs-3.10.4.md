
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: bb396ee
- commit date: 2023-03-11
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                   |
| chameleon      | 9.17 ms                                                | 6.37 ms: 1.44x faster                                  |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.24x faster                                 |
| html5lib       | 85.9 ms                                                | 61.6 ms: 1.39x faster                                  |
| tornado_http   | 128 ms                                                 | 91.2 ms: 1.41x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.1 ms: 1.56x faster                                  |
| float          | 109 ms                                                 | 74.1 ms: 1.47x faster                                  |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                  |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.66 ms: 1.15x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                   |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.48 ms: 1.42x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 55.8 ms: 1.34x faster                                  |
| json_loads           | 28.7 us                                                | 24.0 us: 1.19x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.6 ms: 1.16x faster                                  |
| pickle_list          | 4.72 us                                                | 4.24 us: 1.11x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.10x faster                                   |
| unpickle             | 14.2 us                                                | 13.5 us: 1.05x faster                                  |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                  |
| pickle               | 10.2 us                                                | 10.4 us: 1.03x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.3 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.96 ms: 1.57x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.50 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.1 ms: 1.45x faster                                  |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.8 ms: 1.40x faster                                  |
| genshi_xml      | 63.7 ms                                                | 48.2 ms: 1.32x faster                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.3 ms: 2.52x faster                                  |
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                  |
| logging_silent          | 176 ns                                                 | 95.2 ns: 1.85x faster                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                   |
| asyncio_tcp             | 914 ms                                                 | 502 ms: 1.82x faster                                   |
| richards                | 75.2 ms                                                | 42.9 ms: 1.75x faster                                  |
| pyflate                 | 676 ms                                                 | 403 ms: 1.68x faster                                   |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                   |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 66.5 ms: 1.63x faster                                  |
| spectral_norm           | 150 ms                                                 | 93.3 ms: 1.60x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 73.9 ms: 1.58x faster                                  |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                   |
| python_startup          | 14.1 ms                                                | 8.96 ms: 1.57x faster                                  |
| nbody                   | 144 ms                                                 | 92.1 ms: 1.56x faster                                  |
| chaos                   | 106 ms                                                 | 67.8 ms: 1.56x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.17 ms: 1.53x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                   |
| deepcopy_memo           | 51.7 us                                                | 34.8 us: 1.49x faster                                  |
| float                   | 109 ms                                                 | 74.1 ms: 1.47x faster                                  |
| mako                    | 14.7 ms                                                | 10.1 ms: 1.45x faster                                  |
| chameleon               | 9.17 ms                                                | 6.37 ms: 1.44x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 41.3 ns: 1.44x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                 |
| json_dumps              | 13.4 ms                                                | 9.48 ms: 1.42x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                  |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                  |
| scimark_lu              | 161 ms                                                 | 114 ms: 1.41x faster                                   |
| tornado_http            | 128 ms                                                 | 91.2 ms: 1.41x faster                                  |
| genshi_text             | 30.6 ms                                                | 21.8 ms: 1.40x faster                                  |
| logging_simple          | 8.10 us                                                | 5.77 us: 1.40x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 680 ms: 1.40x faster                                   |
| html5lib                | 85.9 ms                                                | 61.6 ms: 1.39x faster                                  |
| coroutines              | 31.6 ms                                                | 22.7 ms: 1.39x faster                                  |
| logging_format          | 8.85 us                                                | 6.36 us: 1.39x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.28 sec: 1.39x faster                                 |
| fannkuch                | 488 ms                                                 | 355 ms: 1.37x faster                                   |
| async_tree_none         | 711 ms                                                 | 520 ms: 1.37x faster                                   |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.36x faster                                 |
| scimark_fft             | 421 ms                                                 | 313 ms: 1.35x faster                                   |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                   |
| xml_etree_process       | 74.5 ms                                                | 55.8 ms: 1.34x faster                                  |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                  |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                   |
| thrift                  | 1.03 ms                                                | 782 us: 1.32x faster                                   |
| genshi_xml              | 63.7 ms                                                | 48.2 ms: 1.32x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 649 ms: 1.32x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.32x faster                                  |
| deepcopy                | 438 us                                                 | 336 us: 1.30x faster                                   |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 738 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 3.00 us: 1.26x faster                                  |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.24x faster                                 |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.7 ms: 1.22x faster                                  |
| nqueens                 | 100 ms                                                 | 83.3 ms: 1.20x faster                                  |
| bench_thread_pool       | 946 us                                                 | 789 us: 1.20x faster                                   |
| json_loads              | 28.7 us                                                | 24.0 us: 1.19x faster                                  |
| dulwich_log             | 75.8 ms                                                | 63.7 ms: 1.19x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.59 ms: 1.19x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 140 ms: 1.18x faster                                   |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                  |
| json                    | 5.35 ms                                                | 4.57 ms: 1.17x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 80.6 ms: 1.16x faster                                  |
| sympy_expand            | 534 ms                                                 | 461 ms: 1.16x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                  |
| sympy_str               | 325 ms                                                 | 284 ms: 1.14x faster                                   |
| create_gc_cycles        | 1.65 ms                                                | 1.45 ms: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                  |
| pickle_list             | 4.72 us                                                | 4.24 us: 1.11x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.63 us: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| sympy_sum               | 183 ms                                                 | 167 ms: 1.10x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.10x faster                                   |
| mdp                     | 2.74 sec                                               | 2.55 sec: 1.08x faster                                 |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                   |
| unpickle                | 14.2 us                                                | 13.5 us: 1.05x faster                                  |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                   |
| telco                   | 6.73 ms                                                | 6.49 ms: 1.04x faster                                  |
| async_generators        | 426 ms                                                 | 415 ms: 1.03x faster                                   |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                   |
| pickle                  | 10.2 us                                                | 10.4 us: 1.03x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.66 ms: 1.04x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.50 ms: 1.13x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.3 us: 1.13x slower                                  |
| dask                    | 436 ms                                                 | 499 ms: 1.14x slower                                   |
| regex_effbot            | 3.19 ms                                                | 3.66 ms: 1.15x slower                                  |
| coverage                | 74.7 ms                                                | 97.3 ms: 1.30x slower                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230311-3.12.0a6+-bb396ee/bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee.json: comprehensions
