
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 206f05a
- commit date: 2023-01-14
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                   |
| chameleon      | 9.17 ms                                                | 6.35 ms: 1.44x faster                                  |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                 |
| html5lib       | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| tornado_http   | 128 ms                                                 | 93.4 ms: 1.37x faster                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.1 ms: 1.51x faster                                  |
| float          | 109 ms                                                 | 72.2 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| regex_dna      | 214 ms                                                 | 201 ms: 1.07x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.39 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 281 us: 1.61x faster                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.40 ms: 1.43x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.6 ms: 1.22x faster                                  |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                  |
| pickle_list          | 4.72 us                                                | 4.08 us: 1.16x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                   |
| unpickle_list        | 4.92 us                                                | 4.97 us: 1.01x slower                                  |
| pickle_dict          | 27.6 us                                                | 30.5 us: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.95 ms: 1.57x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.49 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.2 ms: 1.51x faster                                  |
| mako            | 14.7 ms                                                | 9.90 ms: 1.48x faster                                  |
| django_template | 46.3 ms                                                | 32.0 ms: 1.45x faster                                  |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.23 ms: 2.25x faster                                  |
| logging_silent          | 176 ns                                                 | 90.6 ns: 1.95x faster                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                   |
| richards                | 75.2 ms                                                | 41.1 ms: 1.83x faster                                  |
| asyncio_tcp             | 914 ms                                                 | 505 ms: 1.81x faster                                   |
| go                      | 226 ms                                                 | 132 ms: 1.71x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 63.8 ms: 1.70x faster                                  |
| pyflate                 | 676 ms                                                 | 398 ms: 1.70x faster                                   |
| raytrace                | 467 ms                                                 | 278 ms: 1.68x faster                                   |
| pickle_pure_python      | 452 us                                                 | 281 us: 1.61x faster                                   |
| spectral_norm           | 150 ms                                                 | 93.9 ms: 1.59x faster                                  |
| python_startup          | 14.1 ms                                                | 8.95 ms: 1.57x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 74.3 ms: 1.57x faster                                  |
| chaos                   | 106 ms                                                 | 67.9 ms: 1.55x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.07 ms: 1.55x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 33.7 us: 1.53x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                   |
| nbody                   | 144 ms                                                 | 95.1 ms: 1.51x faster                                  |
| genshi_text             | 30.6 ms                                                | 20.2 ms: 1.51x faster                                  |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.51x faster                                   |
| float                   | 109 ms                                                 | 72.2 ms: 1.51x faster                                  |
| mako                    | 14.7 ms                                                | 9.90 ms: 1.48x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.47x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.67 ms: 1.45x faster                                  |
| html5lib                | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| django_template         | 46.3 ms                                                | 32.0 ms: 1.45x faster                                  |
| chameleon               | 9.17 ms                                                | 6.35 ms: 1.44x faster                                  |
| logging_simple          | 8.10 us                                                | 5.61 us: 1.44x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                 |
| unpack_sequence         | 59.4 ns                                                | 41.3 ns: 1.44x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.40 ms: 1.43x faster                                  |
| logging_format          | 8.85 us                                                | 6.20 us: 1.43x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 670 ms: 1.42x faster                                   |
| pycparser               | 1.53 sec                                               | 1.08 sec: 1.41x faster                                 |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                  |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                   |
| scimark_fft             | 421 ms                                                 | 306 ms: 1.38x faster                                   |
| tornado_http            | 128 ms                                                 | 93.4 ms: 1.37x faster                                  |
| regex_compile           | 177 ms                                                 | 130 ms: 1.37x faster                                   |
| async_tree_memoization  | 855 ms                                                 | 627 ms: 1.36x faster                                   |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                   |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.05 ms: 1.35x faster                                  |
| aiohttp                 | 1.34 ms                                                | 998 us: 1.34x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                  |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                   |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                   |
| fannkuch                | 488 ms                                                 | 371 ms: 1.31x faster                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 732 ms: 1.30x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.5 ms: 1.29x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                  |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                 |
| coroutines              | 31.6 ms                                                | 25.2 ms: 1.25x faster                                  |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.9 ms: 1.23x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.6 ms: 1.22x faster                                  |
| bench_thread_pool       | 946 us                                                 | 779 us: 1.22x faster                                   |
| async_generators        | 426 ms                                                 | 358 ms: 1.19x faster                                   |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 459 ms: 1.16x faster                                   |
| pickle_list             | 4.72 us                                                | 4.08 us: 1.16x faster                                  |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                   |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                  |
| json                    | 5.35 ms                                                | 4.68 ms: 1.14x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                  |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                   |
| telco                   | 6.73 ms                                                | 6.24 ms: 1.08x faster                                  |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                  |
| regex_dna               | 214 ms                                                 | 201 ms: 1.07x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                   |
| mdp                     | 2.74 sec                                               | 2.69 sec: 1.02x faster                                 |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| unpickle_list           | 4.92 us                                                | 4.97 us: 1.01x slower                                  |
| generators              | 76.4 ms                                                | 78.8 ms: 1.03x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.39 ms: 1.06x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.81 ms: 1.08x slower                                  |
| pickle_dict             | 27.6 us                                                | 30.5 us: 1.11x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.49 ms: 1.12x slower                                  |
| dask                    | 436 ms                                                 | 494 ms: 1.13x slower                                   |
| coverage                | 74.7 ms                                                | 98.6 ms: 1.32x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230114-3.12.0a4+-206f05a/bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a.json: mypy
