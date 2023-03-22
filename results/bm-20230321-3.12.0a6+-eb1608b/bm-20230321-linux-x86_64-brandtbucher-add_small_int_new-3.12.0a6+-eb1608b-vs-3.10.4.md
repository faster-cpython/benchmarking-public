
# Results vs. 3.10.4

- fork: brandtbucher
- ref: add_small_int_new
- machine: linux-x86_64
- commit hash: eb1608b
- commit date: 2023-03-21
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                                      |
| chameleon      | 9.17 ms                                                | 6.23 ms: 1.47x faster                                                     |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.25x faster                                                    |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                     |
| tornado_http   | 128 ms                                                 | 91.0 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 85.9 ms: 1.67x faster                                                     |
| float          | 109 ms                                                 | 73.9 ms: 1.47x faster                                                     |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                     |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                                      |
| regex_effbot   | 3.19 ms                                                | 3.38 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                                      |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                      |
| json_dumps           | 13.4 ms                                                | 9.54 ms: 1.41x faster                                                     |
| xml_etree_process    | 74.5 ms                                                | 55.3 ms: 1.35x faster                                                     |
| json_loads           | 28.7 us                                                | 24.3 us: 1.18x faster                                                     |
| xml_etree_generate   | 93.8 ms                                                | 79.8 ms: 1.18x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 98.7 ms: 1.12x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.32 us: 1.09x faster                                                     |
| unpickle             | 14.2 us                                                | 13.5 us: 1.04x faster                                                     |
| unpickle_list        | 4.92 us                                                | 4.96 us: 1.01x slower                                                     |
| pickle               | 10.2 us                                                | 10.5 us: 1.03x slower                                                     |
| pickle_dict          | 27.6 us                                                | 31.6 us: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.90 ms: 1.58x faster                                                     |
| python_startup_no_site | 5.78 ms                                                | 6.51 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                     |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.44x faster                                                     |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                                     |
| genshi_xml      | 63.7 ms                                                | 48.3 ms: 1.32x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.8 ms: 2.57x faster                                                     |
| deltablue               | 7.28 ms                                                | 3.15 ms: 2.31x faster                                                     |
| logging_silent          | 176 ns                                                 | 92.8 ns: 1.90x faster                                                     |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                      |
| richards                | 75.2 ms                                                | 41.7 ms: 1.80x faster                                                     |
| asyncio_tcp             | 914 ms                                                 | 508 ms: 1.80x faster                                                      |
| go                      | 226 ms                                                 | 130 ms: 1.73x faster                                                      |
| nbody                   | 144 ms                                                 | 85.9 ms: 1.67x faster                                                     |
| raytrace                | 467 ms                                                 | 279 ms: 1.67x faster                                                      |
| scimark_monte_carlo     | 109 ms                                                 | 65.2 ms: 1.66x faster                                                     |
| pyflate                 | 676 ms                                                 | 410 ms: 1.65x faster                                                      |
| chaos                   | 106 ms                                                 | 65.7 ms: 1.61x faster                                                     |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.90 ms: 1.58x faster                                                     |
| spectral_norm           | 150 ms                                                 | 95.6 ms: 1.57x faster                                                     |
| crypto_pyaes            | 117 ms                                                 | 74.7 ms: 1.56x faster                                                     |
| hexiom                  | 9.43 ms                                                | 6.04 ms: 1.56x faster                                                     |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                      |
| deepcopy_memo           | 51.7 us                                                | 34.1 us: 1.52x faster                                                     |
| float                   | 109 ms                                                 | 73.9 ms: 1.47x faster                                                     |
| chameleon               | 9.17 ms                                                | 6.23 ms: 1.47x faster                                                     |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                     |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                      |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.44x faster                                                     |
| logging_simple          | 8.10 us                                                | 5.64 us: 1.44x faster                                                     |
| logging_format          | 8.85 us                                                | 6.20 us: 1.43x faster                                                     |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                     |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                                     |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.42x faster                                                     |
| coroutines              | 31.6 ms                                                | 22.3 ms: 1.42x faster                                                     |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                                    |
| json_dumps              | 13.4 ms                                                | 9.54 ms: 1.41x faster                                                     |
| tornado_http            | 128 ms                                                 | 91.0 ms: 1.41x faster                                                     |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.28 sec: 1.39x faster                                                    |
| pprint_safe_repr        | 953 ms                                                 | 689 ms: 1.38x faster                                                      |
| scimark_fft             | 421 ms                                                 | 308 ms: 1.37x faster                                                      |
| async_tree_none         | 711 ms                                                 | 521 ms: 1.36x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 43.5 ns: 1.36x faster                                                     |
| async_tree_memoization  | 855 ms                                                 | 628 ms: 1.36x faster                                                      |
| deepcopy                | 438 us                                                 | 323 us: 1.35x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 55.3 ms: 1.35x faster                                                     |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                                      |
| thrift                  | 1.03 ms                                                | 773 us: 1.34x faster                                                      |
| fannkuch                | 488 ms                                                 | 365 ms: 1.34x faster                                                      |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                    |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                      |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                     |
| genshi_xml              | 63.7 ms                                                | 48.3 ms: 1.32x faster                                                     |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.31x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.18 ms: 1.31x faster                                                     |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                      |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 741 ms: 1.28x faster                                                      |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                                     |
| nqueens                 | 100 ms                                                 | 79.4 ms: 1.26x faster                                                     |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.25x faster                                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                      |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.7 ms: 1.21x faster                                                     |
| bench_thread_pool       | 946 us                                                 | 788 us: 1.20x faster                                                      |
| dulwich_log             | 75.8 ms                                                | 63.6 ms: 1.19x faster                                                     |
| json_loads              | 28.7 us                                                | 24.3 us: 1.18x faster                                                     |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                     |
| xml_etree_generate      | 93.8 ms                                                | 79.8 ms: 1.18x faster                                                     |
| json                    | 5.35 ms                                                | 4.61 ms: 1.16x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                     |
| sympy_expand            | 534 ms                                                 | 465 ms: 1.15x faster                                                      |
| sympy_str               | 325 ms                                                 | 284 ms: 1.15x faster                                                      |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                                     |
| mdp                     | 2.74 sec                                               | 2.43 sec: 1.13x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 98.7 ms: 1.12x faster                                                     |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                                     |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.49 ms: 1.11x faster                                                     |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                      |
| pickle_list             | 4.72 us                                                | 4.32 us: 1.09x faster                                                     |
| telco                   | 6.73 ms                                                | 6.42 ms: 1.05x faster                                                     |
| unpickle                | 14.2 us                                                | 13.5 us: 1.04x faster                                                     |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                                      |
| async_generators        | 426 ms                                                 | 416 ms: 1.02x faster                                                      |
| unpickle_list           | 4.92 us                                                | 4.96 us: 1.01x slower                                                     |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                      |
| pickle                  | 10.2 us                                                | 10.5 us: 1.03x slower                                                     |
| regex_effbot            | 3.19 ms                                                | 3.38 ms: 1.06x slower                                                     |
| python_startup_no_site  | 5.78 ms                                                | 6.51 ms: 1.13x slower                                                     |
| gc_traversal            | 3.53 ms                                                | 3.98 ms: 1.13x slower                                                     |
| pickle_dict             | 27.6 us                                                | 31.6 us: 1.14x slower                                                     |
| dask                    | 436 ms                                                 | 502 ms: 1.15x slower                                                      |
| coverage                | 74.7 ms                                                | 94.0 ms: 1.26x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230321-3.12.0a6+-eb1608b/bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b.json: comprehensions
