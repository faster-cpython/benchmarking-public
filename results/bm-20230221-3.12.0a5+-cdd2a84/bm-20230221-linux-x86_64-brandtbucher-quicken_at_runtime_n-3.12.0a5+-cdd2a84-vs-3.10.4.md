
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime_n
- machine: linux-x86_64
- commit hash: cdd2a84
- commit date: 2023-02-21
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 247 ms: 1.36x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                        |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.7 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                 | 72.6 ms: 1.50x faster                                                        |
| nbody          | 144 ms                                                 | 96.0 ms: 1.50x faster                                                        |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.14x faster                                                        |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                         |
| regex_effbot   | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 195 us: 1.55x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.45 ms: 1.42x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 54.6 ms: 1.36x faster                                                        |
| json_loads           | 28.7 us                                                | 23.6 us: 1.21x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 80.0 ms: 1.17x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 99.3 ms: 1.12x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.30 us: 1.10x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                         |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                                        |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                                        |
| unpickle_list        | 4.92 us                                                | 4.99 us: 1.01x slower                                                        |
| pickle_dict          | 27.6 us                                                | 32.4 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.81 ms: 1.60x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.34 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.21x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.82 ms: 1.49x faster                                                        |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                        |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 46.5 ms: 1.37x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.5 ms: 2.59x faster                                                        |
| deltablue               | 7.28 ms                                                | 3.16 ms: 2.31x faster                                                        |
| logging_silent          | 176 ns                                                 | 92.9 ns: 1.90x faster                                                        |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                                         |
| asyncio_tcp             | 914 ms                                                 | 503 ms: 1.82x faster                                                         |
| richards                | 75.2 ms                                                | 42.0 ms: 1.79x faster                                                        |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                                         |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                         |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                 | 66.5 ms: 1.63x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.81 ms: 1.60x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                                         |
| crypto_pyaes            | 117 ms                                                 | 73.1 ms: 1.60x faster                                                        |
| chaos                   | 106 ms                                                 | 66.4 ms: 1.59x faster                                                        |
| hexiom                  | 9.43 ms                                                | 5.95 ms: 1.59x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 195 us: 1.55x faster                                                         |
| spectral_norm           | 150 ms                                                 | 96.8 ms: 1.55x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                                        |
| float                   | 109 ms                                                 | 72.6 ms: 1.50x faster                                                        |
| nbody                   | 144 ms                                                 | 96.0 ms: 1.50x faster                                                        |
| mako                    | 14.7 ms                                                | 9.82 ms: 1.49x faster                                                        |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                         |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.43x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.45 ms: 1.42x faster                                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 676 ms: 1.41x faster                                                         |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                                       |
| logging_format          | 8.85 us                                                | 6.33 us: 1.40x faster                                                        |
| logging_simple          | 8.10 us                                                | 5.80 us: 1.40x faster                                                        |
| coroutines              | 31.6 ms                                                | 22.8 ms: 1.39x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 43.1 ns: 1.38x faster                                                        |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                         |
| genshi_xml              | 63.7 ms                                                | 46.5 ms: 1.37x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 54.6 ms: 1.36x faster                                                        |
| 2to3                    | 335 ms                                                 | 247 ms: 1.36x faster                                                         |
| thrift                  | 1.03 ms                                                | 764 us: 1.35x faster                                                         |
| tornado_http            | 128 ms                                                 | 94.7 ms: 1.35x faster                                                        |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                       |
| scimark_fft             | 421 ms                                                 | 314 ms: 1.34x faster                                                         |
| fannkuch                | 488 ms                                                 | 364 ms: 1.34x faster                                                         |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                                         |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.31x faster                                                         |
| async_tree_memoization  | 855 ms                                                 | 656 ms: 1.30x faster                                                         |
| sqlglot_optimize        | 65.2 ms                                                | 50.4 ms: 1.30x faster                                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.93 us: 1.29x faster                                                        |
| mypy2                   | 430 ms                                                 | 332 ms: 1.29x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.23 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 739 ms: 1.28x faster                                                         |
| nqueens                 | 100 ms                                                 | 78.2 ms: 1.28x faster                                                        |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| json_loads              | 28.7 us                                                | 23.6 us: 1.21x faster                                                        |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.8 ms: 1.20x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                         |
| dulwich_log             | 75.8 ms                                                | 63.3 ms: 1.20x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 792 us: 1.19x faster                                                         |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                        |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                                         |
| json                    | 5.35 ms                                                | 4.55 ms: 1.18x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 80.0 ms: 1.17x faster                                                        |
| sympy_str               | 325 ms                                                 | 284 ms: 1.15x faster                                                         |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.14x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                        |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                                        |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.12x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 99.3 ms: 1.12x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                        |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.11x faster                                                         |
| pickle_list             | 4.72 us                                                | 4.30 us: 1.10x faster                                                        |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                         |
| mdp                     | 2.74 sec                                               | 2.51 sec: 1.09x faster                                                       |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                                        |
| async_generators        | 426 ms                                                 | 408 ms: 1.05x faster                                                         |
| telco                   | 6.73 ms                                                | 6.50 ms: 1.04x faster                                                        |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                         |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                                        |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| unpickle_list           | 4.92 us                                                | 4.99 us: 1.01x slower                                                        |
| gc_traversal            | 3.53 ms                                                | 3.67 ms: 1.04x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.34 ms: 1.10x slower                                                        |
| dask                    | 436 ms                                                 | 502 ms: 1.15x slower                                                         |
| pickle_dict             | 27.6 us                                                | 32.4 us: 1.17x slower                                                        |
| coverage                | 74.7 ms                                                | 96.4 ms: 1.29x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
