
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 6b312e0
- commit date: 2023-02-03
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| chameleon      | 9.17 ms                                                | 6.28 ms: 1.46x faster                                               |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 59.5 ms: 1.44x faster                                               |
| tornado_http   | 128 ms                                                 | 94.0 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                               |
| nbody          | 144 ms                                                 | 96.7 ms: 1.49x faster                                               |
| pidigits       | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.11x faster                                               |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                |
| regex_effbot   | 3.19 ms                                                | 3.44 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                                |
| unpickle_pure_python | 302 us                                                 | 200 us: 1.51x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.52 ms: 1.41x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.40x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 77.6 ms: 1.21x faster                                               |
| pickle_list          | 4.72 us                                                | 3.92 us: 1.20x faster                                               |
| json_loads           | 28.7 us                                                | 23.8 us: 1.20x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                               |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                               |
| unpickle_list        | 4.92 us                                                | 5.02 us: 1.02x slower                                               |
| pickle_dict          | 27.6 us                                                | 29.8 us: 1.08x slower                                               |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.96 ms: 1.57x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.48 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.58 ms: 1.53x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                               |
| django_template | 46.3 ms                                                | 32.3 ms: 1.44x faster                                               |
| genshi_xml      | 63.7 ms                                                | 47.9 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.18 ms: 2.29x faster                                               |
| logging_silent          | 176 ns                                                 | 92.7 ns: 1.90x faster                                               |
| asyncio_tcp             | 914 ms                                                 | 496 ms: 1.84x faster                                                |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                                |
| richards                | 75.2 ms                                                | 41.8 ms: 1.80x faster                                               |
| go                      | 226 ms                                                 | 132 ms: 1.71x faster                                                |
| chaos                   | 106 ms                                                 | 63.5 ms: 1.66x faster                                               |
| raytrace                | 467 ms                                                 | 285 ms: 1.64x faster                                                |
| pyflate                 | 676 ms                                                 | 414 ms: 1.63x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 66.5 ms: 1.63x faster                                               |
| hexiom                  | 9.43 ms                                                | 5.94 ms: 1.59x faster                                               |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                                |
| python_startup          | 14.1 ms                                                | 8.96 ms: 1.57x faster                                               |
| mako                    | 14.7 ms                                                | 9.58 ms: 1.53x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 76.4 ms: 1.53x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 200 us: 1.51x faster                                                |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                               |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                |
| nbody                   | 144 ms                                                 | 96.7 ms: 1.49x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                               |
| chameleon               | 9.17 ms                                                | 6.28 ms: 1.46x faster                                               |
| spectral_norm           | 150 ms                                                 | 103 ms: 1.45x faster                                                |
| html5lib                | 85.9 ms                                                | 59.5 ms: 1.44x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                              |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.44x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.43x faster                                               |
| logging_simple          | 8.10 us                                                | 5.70 us: 1.42x faster                                               |
| json_dumps              | 13.4 ms                                                | 9.52 ms: 1.41x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 676 ms: 1.41x faster                                                |
| logging_format          | 8.85 us                                                | 6.28 us: 1.41x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.40x faster                                               |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                                |
| thrift                  | 1.03 ms                                                | 747 us: 1.39x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.98 ms: 1.37x faster                                               |
| scimark_fft             | 421 ms                                                 | 308 ms: 1.37x faster                                                |
| tornado_http            | 128 ms                                                 | 94.0 ms: 1.36x faster                                               |
| deepcopy                | 438 us                                                 | 324 us: 1.35x faster                                                |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.35x faster                                              |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.35x faster                                                |
| async_tree_none         | 711 ms                                                 | 528 ms: 1.35x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                              |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                               |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| genshi_xml              | 63.7 ms                                                | 47.9 ms: 1.33x faster                                               |
| nqueens                 | 100 ms                                                 | 75.8 ms: 1.32x faster                                               |
| deepcopy_reduce         | 3.79 us                                                | 2.88 us: 1.32x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 652 ms: 1.31x faster                                                |
| fannkuch                | 488 ms                                                 | 375 ms: 1.30x faster                                                |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                               |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| unpack_sequence         | 59.4 ns                                                | 46.9 ns: 1.26x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 760 ms: 1.25x faster                                                |
| async_generators        | 426 ms                                                 | 346 ms: 1.23x faster                                                |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                               |
| dulwich_log             | 75.8 ms                                                | 62.3 ms: 1.22x faster                                               |
| coroutines              | 31.6 ms                                                | 26.0 ms: 1.22x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 77.6 ms: 1.21x faster                                               |
| bench_thread_pool       | 946 us                                                 | 784 us: 1.21x faster                                                |
| pickle_list             | 4.72 us                                                | 3.92 us: 1.20x faster                                               |
| json_loads              | 28.7 us                                                | 23.8 us: 1.20x faster                                               |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                |
| sqlite_synth            | 2.92 us                                                | 2.53 us: 1.16x faster                                               |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                               |
| djangocms               | 36.9 us                                                | 32.2 us: 1.14x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                               |
| mdp                     | 2.74 sec                                               | 2.45 sec: 1.12x faster                                              |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.6 ms: 1.11x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                               |
| telco                   | 6.73 ms                                                | 6.46 ms: 1.04x faster                                               |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                |
| generators              | 76.4 ms                                                | 74.5 ms: 1.03x faster                                               |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                               |
| gc_traversal            | 3.53 ms                                                | 3.52 ms: 1.00x faster                                               |
| pidigits                | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| unpickle_list           | 4.92 us                                                | 5.02 us: 1.02x slower                                               |
| regex_effbot            | 3.19 ms                                                | 3.44 ms: 1.08x slower                                               |
| pickle_dict             | 27.6 us                                                | 29.8 us: 1.08x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.48 ms: 1.12x slower                                               |
| dask                    | 436 ms                                                 | 499 ms: 1.14x slower                                                |
| coverage                | 74.7 ms                                                | 99.9 ms: 1.34x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230203-3.12.0a4+-6b312e0/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0.json: mypy
