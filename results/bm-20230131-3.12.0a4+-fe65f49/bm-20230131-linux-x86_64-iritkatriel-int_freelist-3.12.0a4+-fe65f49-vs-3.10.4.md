
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: fe65f49
- commit date: 2023-01-31
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.33x faster                                                |
| chameleon      | 9.17 ms                                                | 6.29 ms: 1.46x faster                                               |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.26x faster                                              |
| html5lib       | 85.9 ms                                                | 61.9 ms: 1.39x faster                                               |
| tornado_http   | 128 ms                                                 | 95.0 ms: 1.35x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 109 ms                                                 | 72.8 ms: 1.50x faster                                               |
| nbody          | 144 ms                                                 | 97.9 ms: 1.47x faster                                               |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                |
| regex_effbot   | 3.19 ms                                                | 3.50 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.58x faster                                                |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.52x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.35 ms: 1.44x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 77.7 ms: 1.21x faster                                               |
| json_loads           | 28.7 us                                                | 24.6 us: 1.17x faster                                               |
| pickle_list          | 4.72 us                                                | 4.09 us: 1.15x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                               |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                               |
| pickle_dict          | 27.6 us                                                | 30.5 us: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.94 ms: 1.58x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.47 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.2 ms: 1.52x faster                                               |
| mako            | 14.7 ms                                                | 9.82 ms: 1.49x faster                                               |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                               |
| genshi_xml      | 63.7 ms                                                | 47.0 ms: 1.36x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.24 ms: 2.25x faster                                               |
| logging_silent          | 176 ns                                                 | 91.3 ns: 1.93x faster                                               |
| asyncio_tcp             | 914 ms                                                 | 496 ms: 1.84x faster                                                |
| richards                | 75.2 ms                                                | 43.8 ms: 1.72x faster                                               |
| go                      | 226 ms                                                 | 138 ms: 1.63x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 67.6 ms: 1.61x faster                                               |
| raytrace                | 467 ms                                                 | 292 ms: 1.60x faster                                                |
| chaos                   | 106 ms                                                 | 66.4 ms: 1.59x faster                                               |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.58x faster                                                |
| python_startup          | 14.1 ms                                                | 8.94 ms: 1.58x faster                                               |
| hexiom                  | 9.43 ms                                                | 5.99 ms: 1.58x faster                                               |
| scimark_sor             | 197 ms                                                 | 125 ms: 1.57x faster                                                |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.52x faster                                                |
| genshi_text             | 30.6 ms                                                | 20.2 ms: 1.52x faster                                               |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                                |
| float                   | 109 ms                                                 | 72.8 ms: 1.50x faster                                               |
| mako                    | 14.7 ms                                                | 9.82 ms: 1.49x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                               |
| nbody                   | 144 ms                                                 | 97.9 ms: 1.47x faster                                               |
| chameleon               | 9.17 ms                                                | 6.29 ms: 1.46x faster                                               |
| pyflate                 | 676 ms                                                 | 467 ms: 1.45x faster                                                |
| json_dumps              | 13.4 ms                                                | 9.35 ms: 1.44x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.42x faster                                              |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                               |
| logging_simple          | 8.10 us                                                | 5.72 us: 1.42x faster                                               |
| logging_format          | 8.85 us                                                | 6.29 us: 1.41x faster                                               |
| thrift                  | 1.03 ms                                                | 735 us: 1.41x faster                                                |
| pprint_safe_repr        | 953 ms                                                 | 678 ms: 1.41x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                               |
| html5lib                | 85.9 ms                                                | 61.9 ms: 1.39x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.48 ms: 1.39x faster                                               |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| unpack_sequence         | 59.4 ns                                                | 43.0 ns: 1.38x faster                                               |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.37x faster                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.78 ms: 1.37x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                              |
| async_tree_none         | 711 ms                                                 | 523 ms: 1.36x faster                                                |
| genshi_xml              | 63.7 ms                                                | 47.0 ms: 1.36x faster                                               |
| tornado_http            | 128 ms                                                 | 95.0 ms: 1.35x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 635 ms: 1.35x faster                                                |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                               |
| 2to3                    | 335 ms                                                 | 253 ms: 1.33x faster                                                |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                               |
| fannkuch                | 488 ms                                                 | 369 ms: 1.32x faster                                                |
| crypto_pyaes            | 117 ms                                                 | 89.5 ms: 1.30x faster                                               |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                |
| sqlglot_optimize        | 65.2 ms                                                | 50.7 ms: 1.29x faster                                               |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                               |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.26x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 752 ms: 1.26x faster                                                |
| nqueens                 | 100 ms                                                 | 79.3 ms: 1.26x faster                                               |
| coroutines              | 31.6 ms                                                | 25.5 ms: 1.24x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.48 ms: 1.22x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 77.7 ms: 1.21x faster                                               |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                |
| bench_thread_pool       | 946 us                                                 | 800 us: 1.18x faster                                                |
| dulwich_log             | 75.8 ms                                                | 64.3 ms: 1.18x faster                                               |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                                |
| json_loads              | 28.7 us                                                | 24.6 us: 1.17x faster                                               |
| pickle_list             | 4.72 us                                                | 4.09 us: 1.15x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| async_generators        | 426 ms                                                 | 372 ms: 1.15x faster                                                |
| json                    | 5.35 ms                                                | 4.67 ms: 1.14x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.45 ms: 1.14x faster                                               |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                |
| sqlite_synth            | 2.92 us                                                | 2.70 us: 1.08x faster                                               |
| scimark_fft             | 421 ms                                                 | 397 ms: 1.06x faster                                                |
| spectral_norm           | 150 ms                                                 | 141 ms: 1.06x faster                                                |
| telco                   | 6.73 ms                                                | 6.37 ms: 1.06x faster                                               |
| pathlib                 | 20.0 ms                                                | 19.0 ms: 1.05x faster                                               |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                               |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                |
| mdp                     | 2.74 sec                                               | 2.72 sec: 1.01x faster                                              |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                               |
| generators              | 76.4 ms                                                | 81.0 ms: 1.06x slower                                               |
| gc_traversal            | 3.53 ms                                                | 3.82 ms: 1.08x slower                                               |
| regex_effbot            | 3.19 ms                                                | 3.50 ms: 1.10x slower                                               |
| pickle_dict             | 27.6 us                                                | 30.5 us: 1.11x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.47 ms: 1.12x slower                                               |
| dask                    | 436 ms                                                 | 526 ms: 1.21x slower                                                |
| coverage                | 74.7 ms                                                | 95.1 ms: 1.27x slower                                               |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                        |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230131-3.12.0a4+-fe65f49/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49.json: mypy
