
# Results vs. 3.10.4

- fork: python
- ref: 84e20c689a8b3b6cebfd
- machine: linux-x86_64
- commit hash: 84e20c6
- commit date: 2023-03-16
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.47 ms: 1.42x faster                                                  |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.7 ms: 1.42x faster                                                  |
| tornado_http   | 128 ms                                                 | 91.0 ms: 1.41x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 88.8 ms: 1.62x faster                                                  |
| float          | 109 ms                                                 | 73.7 ms: 1.48x faster                                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                  |
| regex_dna      | 214 ms                                                 | 200 ms: 1.07x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.62 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 280 us: 1.61x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 56.1 ms: 1.33x faster                                                  |
| json_loads           | 28.7 us                                                | 24.0 us: 1.19x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 81.1 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 98.5 ms: 1.13x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.28 us: 1.10x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                  |
| unpickle_list        | 4.92 us                                                | 5.08 us: 1.03x slower                                                  |
| pickle               | 10.2 us                                                | 10.5 us: 1.04x slower                                                  |
| pickle_dict          | 27.6 us                                                | 31.0 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.93 ms: 1.58x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.52 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                  |
| genshi_text     | 30.6 ms                                                | 21.5 ms: 1.42x faster                                                  |
| django_template | 46.3 ms                                                | 33.5 ms: 1.38x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 47.5 ms: 1.34x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.5 ms: 2.59x faster                                                  |
| deltablue               | 7.28 ms                                                | 3.15 ms: 2.31x faster                                                  |
| logging_silent          | 176 ns                                                 | 93.4 ns: 1.89x faster                                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                   |
| asyncio_tcp             | 914 ms                                                 | 507 ms: 1.80x faster                                                   |
| richards                | 75.2 ms                                                | 42.0 ms: 1.79x faster                                                  |
| go                      | 226 ms                                                 | 132 ms: 1.71x faster                                                   |
| raytrace                | 467 ms                                                 | 278 ms: 1.68x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 66.0 ms: 1.64x faster                                                  |
| pyflate                 | 676 ms                                                 | 412 ms: 1.64x faster                                                   |
| spectral_norm           | 150 ms                                                 | 92.3 ms: 1.62x faster                                                  |
| nbody                   | 144 ms                                                 | 88.8 ms: 1.62x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 280 us: 1.61x faster                                                   |
| chaos                   | 106 ms                                                 | 66.0 ms: 1.60x faster                                                  |
| python_startup          | 14.1 ms                                                | 8.93 ms: 1.58x faster                                                  |
| deepcopy_memo           | 51.7 us                                                | 33.1 us: 1.56x faster                                                  |
| crypto_pyaes            | 117 ms                                                 | 75.1 ms: 1.55x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.10 ms: 1.55x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                   |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.48x faster                                                   |
| float                   | 109 ms                                                 | 73.7 ms: 1.48x faster                                                  |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                                  |
| logging_simple          | 8.10 us                                                | 5.62 us: 1.44x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.42x faster                                                  |
| logging_format          | 8.85 us                                                | 6.22 us: 1.42x faster                                                  |
| genshi_text             | 30.6 ms                                                | 21.5 ms: 1.42x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                                 |
| chameleon               | 9.17 ms                                                | 6.47 ms: 1.42x faster                                                  |
| html5lib                | 85.9 ms                                                | 60.7 ms: 1.42x faster                                                  |
| tornado_http            | 128 ms                                                 | 91.0 ms: 1.41x faster                                                  |
| async_tree_io           | 1.78 sec                                               | 1.27 sec: 1.40x faster                                                 |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                                 |
| pprint_safe_repr        | 953 ms                                                 | 682 ms: 1.40x faster                                                   |
| async_tree_memoization  | 855 ms                                                 | 614 ms: 1.39x faster                                                   |
| django_template         | 46.3 ms                                                | 33.5 ms: 1.38x faster                                                  |
| scimark_fft             | 421 ms                                                 | 306 ms: 1.38x faster                                                   |
| async_tree_none         | 711 ms                                                 | 518 ms: 1.37x faster                                                   |
| coroutines              | 31.6 ms                                                | 23.1 ms: 1.37x faster                                                  |
| deepcopy                | 438 us                                                 | 324 us: 1.35x faster                                                   |
| thrift                  | 1.03 ms                                                | 769 us: 1.34x faster                                                   |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                                   |
| unpack_sequence         | 59.4 ns                                                | 44.2 ns: 1.34x faster                                                  |
| genshi_xml              | 63.7 ms                                                | 47.5 ms: 1.34x faster                                                  |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                  |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 56.1 ms: 1.33x faster                                                  |
| fannkuch                | 488 ms                                                 | 367 ms: 1.33x faster                                                   |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.17 ms: 1.31x faster                                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.91 us: 1.30x faster                                                  |
| mypy2                   | 430 ms                                                 | 332 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 736 ms: 1.29x faster                                                   |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                                  |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                 |
| nqueens                 | 100 ms                                                 | 79.9 ms: 1.25x faster                                                  |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.6 ms: 1.22x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                   |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.20x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 791 us: 1.20x faster                                                   |
| json_loads              | 28.7 us                                                | 24.0 us: 1.19x faster                                                  |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                  |
| json                    | 5.35 ms                                                | 4.59 ms: 1.16x faster                                                  |
| sympy_expand            | 534 ms                                                 | 459 ms: 1.16x faster                                                   |
| xml_etree_generate      | 93.8 ms                                                | 81.1 ms: 1.16x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                  |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                                   |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                                  |
| mdp                     | 2.74 sec                                               | 2.43 sec: 1.13x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                 | 98.5 ms: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                                  |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.11x faster                                                   |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                   |
| pickle_list             | 4.72 us                                                | 4.28 us: 1.10x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| regex_dna               | 214 ms                                                 | 200 ms: 1.07x faster                                                   |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                  |
| telco                   | 6.73 ms                                                | 6.46 ms: 1.04x faster                                                  |
| async_generators        | 426 ms                                                 | 410 ms: 1.04x faster                                                   |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                   |
| unpickle_list           | 4.92 us                                                | 5.08 us: 1.03x slower                                                  |
| pickle                  | 10.2 us                                                | 10.5 us: 1.04x slower                                                  |
| gc_traversal            | 3.53 ms                                                | 3.67 ms: 1.04x slower                                                  |
| pickle_dict             | 27.6 us                                                | 31.0 us: 1.12x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.52 ms: 1.13x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.62 ms: 1.13x slower                                                  |
| dask                    | 436 ms                                                 | 500 ms: 1.15x slower                                                   |
| coverage                | 74.7 ms                                                | 94.2 ms: 1.26x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230316-3.12.0a6+-84e20c6/bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6.json: comprehensions
