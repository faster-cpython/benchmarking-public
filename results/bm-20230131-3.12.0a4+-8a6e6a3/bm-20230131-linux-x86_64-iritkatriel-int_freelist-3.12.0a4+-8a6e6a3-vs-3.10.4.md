
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 8a6e6a3
- commit date: 2023-01-31
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| chameleon      | 9.17 ms                                                | 6.37 ms: 1.44x faster                                               |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 61.6 ms: 1.39x faster                                               |
| tornado_http   | 128 ms                                                 | 95.3 ms: 1.35x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 96.3 ms: 1.49x faster                                               |
| float          | 109 ms                                                 | 73.8 ms: 1.48x faster                                               |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.40x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                               |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                |
| regex_effbot   | 3.19 ms                                                | 3.47 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                                |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.50 ms: 1.42x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 77.4 ms: 1.21x faster                                               |
| json_loads           | 28.7 us                                                | 24.7 us: 1.16x faster                                               |
| pickle_list          | 4.72 us                                                | 4.23 us: 1.12x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| pickle_dict          | 27.6 us                                                | 31.8 us: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmark hidden because not significant (3): unpickle, pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.97 ms: 1.57x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.49 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.80 ms: 1.50x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                               |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| genshi_xml      | 63.7 ms                                                | 47.4 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.25 ms: 2.24x faster                                               |
| logging_silent          | 176 ns                                                 | 92.4 ns: 1.91x faster                                               |
| asyncio_tcp             | 914 ms                                                 | 498 ms: 1.84x faster                                                |
| richards                | 75.2 ms                                                | 43.2 ms: 1.74x faster                                               |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                |
| chaos                   | 106 ms                                                 | 64.4 ms: 1.64x faster                                               |
| scimark_monte_carlo     | 109 ms                                                 | 66.4 ms: 1.63x faster                                               |
| raytrace                | 467 ms                                                 | 291 ms: 1.61x faster                                                |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.60x faster                                                |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                                |
| hexiom                  | 9.43 ms                                                | 5.98 ms: 1.58x faster                                               |
| python_startup          | 14.1 ms                                                | 8.97 ms: 1.57x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.51x faster                                                |
| mako                    | 14.7 ms                                                | 9.80 ms: 1.50x faster                                               |
| nbody                   | 144 ms                                                 | 96.3 ms: 1.49x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.9 us: 1.48x faster                                               |
| float                   | 109 ms                                                 | 73.8 ms: 1.48x faster                                               |
| pyflate                 | 676 ms                                                 | 461 ms: 1.46x faster                                                |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                              |
| chameleon               | 9.17 ms                                                | 6.37 ms: 1.44x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 669 ms: 1.43x faster                                                |
| json_dumps              | 13.4 ms                                                | 9.50 ms: 1.42x faster                                               |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| regex_compile           | 177 ms                                                 | 127 ms: 1.40x faster                                                |
| logging_simple          | 8.10 us                                                | 5.79 us: 1.40x faster                                               |
| html5lib                | 85.9 ms                                                | 61.6 ms: 1.39x faster                                               |
| logging_format          | 8.85 us                                                | 6.35 us: 1.39x faster                                               |
| unpack_sequence         | 59.4 ns                                                | 42.7 ns: 1.39x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.48 ms: 1.38x faster                                               |
| thrift                  | 1.03 ms                                                | 751 us: 1.38x faster                                                |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.37x faster                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.78 ms: 1.36x faster                                               |
| fannkuch                | 488 ms                                                 | 360 ms: 1.36x faster                                                |
| async_tree_none         | 711 ms                                                 | 528 ms: 1.35x faster                                                |
| tornado_http            | 128 ms                                                 | 95.3 ms: 1.35x faster                                               |
| genshi_xml              | 63.7 ms                                                | 47.4 ms: 1.34x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                              |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                               |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                               |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                                |
| nqueens                 | 100 ms                                                 | 76.2 ms: 1.31x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 659 ms: 1.30x faster                                                |
| crypto_pyaes            | 117 ms                                                 | 90.0 ms: 1.30x faster                                               |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.28x faster                                               |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| deepcopy_reduce         | 3.79 us                                                | 3.02 us: 1.25x faster                                               |
| coroutines              | 31.6 ms                                                | 25.3 ms: 1.25x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 761 ms: 1.25x faster                                                |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 77.4 ms: 1.21x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.55 ms: 1.20x faster                                               |
| sympy_str               | 325 ms                                                 | 271 ms: 1.20x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                               |
| bench_thread_pool       | 946 us                                                 | 801 us: 1.18x faster                                                |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                |
| dulwich_log             | 75.8 ms                                                | 64.4 ms: 1.18x faster                                               |
| sympy_expand            | 534 ms                                                 | 459 ms: 1.16x faster                                                |
| json_loads              | 28.7 us                                                | 24.7 us: 1.16x faster                                               |
| async_generators        | 426 ms                                                 | 369 ms: 1.16x faster                                                |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                               |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                               |
| pickle_list             | 4.72 us                                                | 4.23 us: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                |
| sqlite_synth            | 2.92 us                                                | 2.68 us: 1.09x faster                                               |
| spectral_norm           | 150 ms                                                 | 138 ms: 1.08x faster                                                |
| mdp                     | 2.74 sec                                               | 2.53 sec: 1.08x faster                                              |
| scimark_fft             | 421 ms                                                 | 390 ms: 1.08x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| pathlib                 | 20.0 ms                                                | 18.9 ms: 1.06x faster                                               |
| telco                   | 6.73 ms                                                | 6.43 ms: 1.05x faster                                               |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| gc_traversal            | 3.53 ms                                                | 3.81 ms: 1.08x slower                                               |
| regex_effbot            | 3.19 ms                                                | 3.47 ms: 1.09x slower                                               |
| generators              | 76.4 ms                                                | 83.5 ms: 1.09x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.49 ms: 1.12x slower                                               |
| pickle_dict             | 27.6 us                                                | 31.8 us: 1.15x slower                                               |
| dask                    | 436 ms                                                 | 525 ms: 1.20x slower                                                |
| coverage                | 74.7 ms                                                | 96.1 ms: 1.29x slower                                               |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                        |

Benchmark hidden because not significant (4): unpickle, pickle, bench_mp_pool, unpickle_list
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230131-3.12.0a4+-8a6e6a3/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3.json: mypy
