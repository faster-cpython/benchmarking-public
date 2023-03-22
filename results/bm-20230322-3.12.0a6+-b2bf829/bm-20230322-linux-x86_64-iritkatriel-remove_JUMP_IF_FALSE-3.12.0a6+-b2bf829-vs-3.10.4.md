
# Results vs. 3.10.4

- fork: iritkatriel
- ref: remove_JUMP_IF_FALSE
- machine: linux-x86_64
- commit hash: b2bf829
- commit date: 2023-03-22
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.35x faster                                                        |
| chameleon      | 9.17 ms                                                | 6.39 ms: 1.43x faster                                                       |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                      |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                                       |
| tornado_http   | 128 ms                                                 | 91.3 ms: 1.40x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 87.1 ms: 1.65x faster                                                       |
| float          | 109 ms                                                 | 74.1 ms: 1.47x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                                        |
| regex_effbot   | 3.19 ms                                                | 3.43 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.59x faster                                                        |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                        |
| json_dumps           | 13.4 ms                                                | 9.46 ms: 1.42x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 56.1 ms: 1.33x faster                                                       |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                       |
| xml_etree_generate   | 93.8 ms                                                | 80.7 ms: 1.16x faster                                                       |
| pickle_list          | 4.72 us                                                | 4.11 us: 1.15x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                        |
| unpickle_list        | 4.92 us                                                | 4.99 us: 1.01x slower                                                       |
| pickle_dict          | 27.6 us                                                | 31.9 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.81 ms: 1.60x faster                                                       |
| python_startup_no_site | 5.78 ms                                                | 6.51 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.94 ms: 1.47x faster                                                       |
| genshi_text     | 30.6 ms                                                | 21.7 ms: 1.41x faster                                                       |
| django_template | 46.3 ms                                                | 33.4 ms: 1.39x faster                                                       |
| genshi_xml      | 63.7 ms                                                | 47.4 ms: 1.34x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.0 ms: 2.63x faster                                                       |
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                       |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.87x faster                                                        |
| logging_silent          | 176 ns                                                 | 96.6 ns: 1.83x faster                                                       |
| asyncio_tcp             | 914 ms                                                 | 506 ms: 1.81x faster                                                        |
| richards                | 75.2 ms                                                | 43.9 ms: 1.71x faster                                                       |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 64.7 ms: 1.68x faster                                                       |
| spectral_norm           | 150 ms                                                 | 89.6 ms: 1.67x faster                                                       |
| pyflate                 | 676 ms                                                 | 407 ms: 1.66x faster                                                        |
| nbody                   | 144 ms                                                 | 87.1 ms: 1.65x faster                                                       |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                                        |
| chaos                   | 106 ms                                                 | 65.4 ms: 1.62x faster                                                       |
| python_startup          | 14.1 ms                                                | 8.81 ms: 1.60x faster                                                       |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.59x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 74.1 ms: 1.57x faster                                                       |
| hexiom                  | 9.43 ms                                                | 6.11 ms: 1.54x faster                                                       |
| deepcopy_memo           | 51.7 us                                                | 33.7 us: 1.53x faster                                                       |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                        |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                        |
| mako                    | 14.7 ms                                                | 9.94 ms: 1.47x faster                                                       |
| float                   | 109 ms                                                 | 74.1 ms: 1.47x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.39 ms: 1.43x faster                                                       |
| scimark_fft             | 421 ms                                                 | 296 ms: 1.42x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.46 ms: 1.42x faster                                                       |
| coroutines              | 31.6 ms                                                | 22.3 ms: 1.42x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 42.0 ns: 1.42x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                                       |
| genshi_text             | 30.6 ms                                                | 21.7 ms: 1.41x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                                       |
| tornado_http            | 128 ms                                                 | 91.3 ms: 1.40x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.75 ms: 1.39x faster                                                       |
| django_template         | 46.3 ms                                                | 33.4 ms: 1.39x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.43 sec: 1.39x faster                                                      |
| logging_format          | 8.85 us                                                | 6.41 us: 1.38x faster                                                       |
| logging_simple          | 8.10 us                                                | 5.87 us: 1.38x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                      |
| pprint_safe_repr        | 953 ms                                                 | 695 ms: 1.37x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.36x faster                                                      |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                        |
| 2to3                    | 335 ms                                                 | 248 ms: 1.35x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 47.4 ms: 1.34x faster                                                       |
| deepcopy                | 438 us                                                 | 326 us: 1.34x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.08 ms: 1.34x faster                                                       |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 56.1 ms: 1.33x faster                                                       |
| thrift                  | 1.03 ms                                                | 780 us: 1.33x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                       |
| fannkuch                | 488 ms                                                 | 372 ms: 1.31x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 653 ms: 1.31x faster                                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.92 us: 1.30x faster                                                       |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 743 ms: 1.28x faster                                                        |
| sqlglot_optimize        | 65.2 ms                                                | 51.4 ms: 1.27x faster                                                       |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                      |
| nqueens                 | 100 ms                                                 | 80.9 ms: 1.24x faster                                                       |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.6 ms: 1.22x faster                                                       |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                       |
| dulwich_log             | 75.8 ms                                                | 63.3 ms: 1.20x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 790 us: 1.20x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                        |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                       |
| json                    | 5.35 ms                                                | 4.54 ms: 1.18x faster                                                       |
| sympy_expand            | 534 ms                                                 | 459 ms: 1.16x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 80.7 ms: 1.16x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                                        |
| pickle_list             | 4.72 us                                                | 4.11 us: 1.15x faster                                                       |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                       |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                       |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.49 ms: 1.11x faster                                                       |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.55 sec: 1.08x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 153 ms: 1.07x faster                                                        |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                                        |
| async_generators        | 426 ms                                                 | 413 ms: 1.03x faster                                                        |
| telco                   | 6.73 ms                                                | 6.60 ms: 1.02x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| unpickle_list           | 4.92 us                                                | 4.99 us: 1.01x slower                                                       |
| regex_effbot            | 3.19 ms                                                | 3.43 ms: 1.07x slower                                                       |
| gc_traversal            | 3.53 ms                                                | 3.98 ms: 1.13x slower                                                       |
| python_startup_no_site  | 5.78 ms                                                | 6.51 ms: 1.13x slower                                                       |
| dask                    | 436 ms                                                 | 503 ms: 1.15x slower                                                        |
| pickle_dict             | 27.6 us                                                | 31.9 us: 1.16x slower                                                       |
| coverage                | 74.7 ms                                                | 95.9 ms: 1.28x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (3): unpickle, bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230322-3.12.0a6+-b2bf829/bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829.json: comprehensions
