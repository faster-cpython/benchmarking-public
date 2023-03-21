
# Results vs. 3.10.4

- fork: itamaro
- ref: eager_tasks_factory
- machine: linux-x86_64
- commit hash: bcf40dc
- commit date: 2023-03-20
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.35x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.27 ms: 1.46x faster                                                  |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 87.6 ms: 1.64x faster                                                  |
| float          | 109 ms                                                 | 74.0 ms: 1.47x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                  |
| regex_dna      | 214 ms                                                 | 204 ms: 1.05x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.30 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 281 us: 1.61x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.51 ms: 1.41x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 55.3 ms: 1.35x faster                                                  |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.1 ms: 1.17x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.21 us: 1.12x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| unpickle             | 14.2 us                                                | 13.4 us: 1.05x faster                                                  |
| unpickle_list        | 4.92 us                                                | 4.97 us: 1.01x slower                                                  |
| pickle               | 10.2 us                                                | 10.4 us: 1.03x slower                                                  |
| pickle_dict          | 27.6 us                                                | 31.3 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.55 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.99 ms: 1.47x faster                                                  |
| genshi_text     | 30.6 ms                                                | 21.0 ms: 1.46x faster                                                  |
| django_template | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 47.8 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.4 ms: 2.60x faster                                                  |
| deltablue               | 7.28 ms                                                | 3.14 ms: 2.31x faster                                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                   |
| logging_silent          | 176 ns                                                 | 96.2 ns: 1.83x faster                                                  |
| asyncio_tcp             | 914 ms                                                 | 506 ms: 1.81x faster                                                   |
| richards                | 75.2 ms                                                | 42.0 ms: 1.79x faster                                                  |
| spectral_norm           | 150 ms                                                 | 88.2 ms: 1.70x faster                                                  |
| pyflate                 | 676 ms                                                 | 403 ms: 1.68x faster                                                   |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.5 ms: 1.66x faster                                                  |
| nbody                   | 144 ms                                                 | 87.6 ms: 1.64x faster                                                  |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                                   |
| chaos                   | 106 ms                                                 | 65.5 ms: 1.61x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 281 us: 1.61x faster                                                   |
| crypto_pyaes            | 117 ms                                                 | 73.2 ms: 1.59x faster                                                  |
| python_startup          | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.08 ms: 1.55x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                   |
| deepcopy_memo           | 51.7 us                                                | 34.0 us: 1.52x faster                                                  |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                                   |
| float                   | 109 ms                                                 | 74.0 ms: 1.47x faster                                                  |
| mako                    | 14.7 ms                                                | 9.99 ms: 1.47x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.27 ms: 1.46x faster                                                  |
| genshi_text             | 30.6 ms                                                | 21.0 ms: 1.46x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                  |
| logging_simple          | 8.10 us                                                | 5.69 us: 1.42x faster                                                  |
| logging_format          | 8.85 us                                                | 6.23 us: 1.42x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                  |
| scimark_fft             | 421 ms                                                 | 297 ms: 1.42x faster                                                   |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.51 ms: 1.41x faster                                                  |
| coroutines              | 31.6 ms                                                | 22.4 ms: 1.41x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                                 |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 687 ms: 1.39x faster                                                   |
| unpack_sequence         | 59.4 ns                                                | 42.9 ns: 1.38x faster                                                  |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                 |
| async_tree_memoization  | 855 ms                                                 | 619 ms: 1.38x faster                                                   |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.37x faster                                                 |
| async_tree_none         | 711 ms                                                 | 521 ms: 1.37x faster                                                   |
| deepcopy                | 438 us                                                 | 323 us: 1.36x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 55.3 ms: 1.35x faster                                                  |
| 2to3                    | 335 ms                                                 | 249 ms: 1.35x faster                                                   |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                   |
| fannkuch                | 488 ms                                                 | 365 ms: 1.34x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 47.8 ms: 1.33x faster                                                  |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                  |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                  |
| thrift                  | 1.03 ms                                                | 788 us: 1.31x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.18 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.30x faster                                                   |
| mypy2                   | 430 ms                                                 | 332 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.6 ms: 1.29x faster                                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 736 ms: 1.29x faster                                                   |
| nqueens                 | 100 ms                                                 | 78.2 ms: 1.28x faster                                                  |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                 |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.6 ms: 1.22x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                   |
| bench_thread_pool       | 946 us                                                 | 783 us: 1.21x faster                                                   |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.21x faster                                                  |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                  |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.19x faster                                                  |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                   |
| xml_etree_generate      | 93.8 ms                                                | 80.1 ms: 1.17x faster                                                  |
| json                    | 5.35 ms                                                | 4.59 ms: 1.16x faster                                                  |
| sympy_str               | 325 ms                                                 | 281 ms: 1.16x faster                                                   |
| djangocms               | 36.9 us                                                | 32.2 us: 1.14x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                  |
| pickle_list             | 4.72 us                                                | 4.21 us: 1.12x faster                                                  |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                                   |
| create_gc_cycles        | 1.65 ms                                                | 1.49 ms: 1.10x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                   |
| mdp                     | 2.74 sec                                               | 2.55 sec: 1.07x faster                                                 |
| telco                   | 6.73 ms                                                | 6.36 ms: 1.06x faster                                                  |
| unpickle                | 14.2 us                                                | 13.4 us: 1.05x faster                                                  |
| regex_dna               | 214 ms                                                 | 204 ms: 1.05x faster                                                   |
| async_generators        | 426 ms                                                 | 411 ms: 1.04x faster                                                   |
| unpickle_list           | 4.92 us                                                | 4.97 us: 1.01x slower                                                  |
| pickle                  | 10.2 us                                                | 10.4 us: 1.03x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.30 ms: 1.03x slower                                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| gc_traversal            | 3.53 ms                                                | 3.98 ms: 1.13x slower                                                  |
| pickle_dict             | 27.6 us                                                | 31.3 us: 1.13x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.55 ms: 1.13x slower                                                  |
| dask                    | 436 ms                                                 | 499 ms: 1.14x slower                                                   |
| coverage                | 74.7 ms                                                | 96.8 ms: 1.29x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230320-3.12.0a6+-bcf40dc/bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc.json: comprehensions
