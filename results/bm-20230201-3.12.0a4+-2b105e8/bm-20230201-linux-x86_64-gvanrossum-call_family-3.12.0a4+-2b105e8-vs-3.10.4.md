
# Results vs. 3.10.4

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: 2b105e8
- commit date: 2023-02-01
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                              |
| chameleon      | 9.17 ms                                                | 6.42 ms: 1.43x faster                                             |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                            |
| html5lib       | 85.9 ms                                                | 59.4 ms: 1.45x faster                                             |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                             |
| Geometric mean | (ref)                                                  | 1.37x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.5 ms: 1.52x faster                                             |
| float          | 109 ms                                                 | 72.8 ms: 1.50x faster                                             |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.40x faster                                              |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.16x faster                                             |
| regex_dna      | 214 ms                                                 | 213 ms: 1.01x faster                                              |
| regex_effbot   | 3.19 ms                                                | 3.62 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                              |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                              |
| json_dumps           | 13.4 ms                                                | 9.40 ms: 1.43x faster                                             |
| xml_etree_process    | 74.5 ms                                                | 53.3 ms: 1.40x faster                                             |
| xml_etree_generate   | 93.8 ms                                                | 77.2 ms: 1.21x faster                                             |
| json_loads           | 28.7 us                                                | 23.8 us: 1.21x faster                                             |
| pickle_list          | 4.72 us                                                | 3.99 us: 1.18x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                              |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                             |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                             |
| unpickle_list        | 4.92 us                                                | 5.03 us: 1.02x slower                                             |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                             |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.95 ms: 1.57x faster                                             |
| python_startup_no_site | 5.78 ms                                                | 6.48 ms: 1.12x slower                                             |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.73 ms: 1.51x faster                                             |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                             |
| django_template | 46.3 ms                                                | 32.1 ms: 1.44x faster                                             |
| genshi_xml      | 63.7 ms                                                | 46.2 ms: 1.38x faster                                             |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.13 ms: 2.32x faster                                             |
| logging_silent          | 176 ns                                                 | 91.1 ns: 1.94x faster                                             |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                              |
| asyncio_tcp             | 914 ms                                                 | 495 ms: 1.85x faster                                              |
| richards                | 75.2 ms                                                | 41.8 ms: 1.80x faster                                             |
| pyflate                 | 676 ms                                                 | 395 ms: 1.71x faster                                              |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                              |
| chaos                   | 106 ms                                                 | 63.0 ms: 1.68x faster                                             |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                              |
| scimark_monte_carlo     | 109 ms                                                 | 65.9 ms: 1.65x faster                                             |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                              |
| hexiom                  | 9.43 ms                                                | 5.94 ms: 1.59x faster                                             |
| crypto_pyaes            | 117 ms                                                 | 73.7 ms: 1.58x faster                                             |
| python_startup          | 14.1 ms                                                | 8.95 ms: 1.57x faster                                             |
| spectral_norm           | 150 ms                                                 | 97.2 ms: 1.54x faster                                             |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                              |
| scimark_lu              | 161 ms                                                 | 105 ms: 1.52x faster                                              |
| nbody                   | 144 ms                                                 | 94.5 ms: 1.52x faster                                             |
| mako                    | 14.7 ms                                                | 9.73 ms: 1.51x faster                                             |
| float                   | 109 ms                                                 | 72.8 ms: 1.50x faster                                             |
| deepcopy_memo           | 51.7 us                                                | 34.9 us: 1.48x faster                                             |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                             |
| html5lib                | 85.9 ms                                                | 59.4 ms: 1.45x faster                                             |
| django_template         | 46.3 ms                                                | 32.1 ms: 1.44x faster                                             |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                            |
| json_dumps              | 13.4 ms                                                | 9.40 ms: 1.43x faster                                             |
| chameleon               | 9.17 ms                                                | 6.42 ms: 1.43x faster                                             |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                             |
| pprint_safe_repr        | 953 ms                                                 | 674 ms: 1.41x faster                                              |
| xml_etree_process       | 74.5 ms                                                | 53.3 ms: 1.40x faster                                             |
| regex_compile           | 177 ms                                                 | 127 ms: 1.40x faster                                              |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.40x faster                                            |
| logging_simple          | 8.10 us                                                | 5.81 us: 1.39x faster                                             |
| unpack_sequence         | 59.4 ns                                                | 42.6 ns: 1.39x faster                                             |
| logging_format          | 8.85 us                                                | 6.37 us: 1.39x faster                                             |
| genshi_xml              | 63.7 ms                                                | 46.2 ms: 1.38x faster                                             |
| thrift                  | 1.03 ms                                                | 751 us: 1.38x faster                                              |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                             |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                            |
| fannkuch                | 488 ms                                                 | 363 ms: 1.35x faster                                              |
| scimark_fft             | 421 ms                                                 | 313 ms: 1.34x faster                                              |
| aiohttp                 | 1.34 ms                                                | 999 us: 1.34x faster                                              |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                              |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                              |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.13 ms: 1.32x faster                                             |
| deepcopy_reduce         | 3.79 us                                                | 2.88 us: 1.31x faster                                             |
| nqueens                 | 100 ms                                                 | 77.3 ms: 1.30x faster                                             |
| coroutines              | 31.6 ms                                                | 24.5 ms: 1.29x faster                                             |
| async_tree_memoization  | 855 ms                                                 | 664 ms: 1.29x faster                                              |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                             |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                              |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                            |
| async_tree_cpu_io_mixed | 949 ms                                                 | 754 ms: 1.26x faster                                              |
| async_generators        | 426 ms                                                 | 348 ms: 1.23x faster                                              |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                             |
| xml_etree_generate      | 93.8 ms                                                | 77.2 ms: 1.21x faster                                             |
| bench_thread_pool       | 946 us                                                 | 779 us: 1.21x faster                                              |
| json_loads              | 28.7 us                                                | 23.8 us: 1.21x faster                                             |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                              |
| dulwich_log             | 75.8 ms                                                | 63.3 ms: 1.20x faster                                             |
| pickle_list             | 4.72 us                                                | 3.99 us: 1.18x faster                                             |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                              |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                              |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.16x faster                                             |
| json                    | 5.35 ms                                                | 4.65 ms: 1.15x faster                                             |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                             |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                             |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                             |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.11x faster                                             |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                              |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                              |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                              |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                             |
| telco                   | 6.73 ms                                                | 6.36 ms: 1.06x faster                                             |
| mdp                     | 2.74 sec                                               | 2.60 sec: 1.05x faster                                            |
| generators              | 76.4 ms                                                | 74.9 ms: 1.02x faster                                             |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                             |
| regex_dna               | 214 ms                                                 | 213 ms: 1.01x faster                                              |
| unpickle_list           | 4.92 us                                                | 5.03 us: 1.02x slower                                             |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                             |
| python_startup_no_site  | 5.78 ms                                                | 6.48 ms: 1.12x slower                                             |
| gc_traversal            | 3.53 ms                                                | 3.96 ms: 1.12x slower                                             |
| regex_effbot            | 3.19 ms                                                | 3.62 ms: 1.13x slower                                             |
| dask                    | 436 ms                                                 | 498 ms: 1.14x slower                                              |
| coverage                | 74.7 ms                                                | 97.1 ms: 1.30x slower                                             |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-2b105e8/bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8.json: mypy
