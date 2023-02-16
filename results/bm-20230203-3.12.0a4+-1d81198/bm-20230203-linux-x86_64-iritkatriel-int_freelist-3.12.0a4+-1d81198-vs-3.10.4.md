
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1d81198
- commit date: 2023-02-03
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| chameleon      | 9.17 ms                                                | 6.28 ms: 1.46x faster                                               |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 60.0 ms: 1.43x faster                                               |
| tornado_http   | 128 ms                                                 | 93.7 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.8 ms: 1.50x faster                                               |
| float          | 109 ms                                                 | 73.2 ms: 1.49x faster                                               |
| pidigits       | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                               |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                                |
| regex_effbot   | 3.19 ms                                                | 3.51 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                                |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.53x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.43 ms: 1.43x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.40x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 77.4 ms: 1.21x faster                                               |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                                |
| pickle_list          | 4.72 us                                                | 4.23 us: 1.12x faster                                               |
| unpickle             | 14.2 us                                                | 12.9 us: 1.09x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| unpickle_list        | 4.92 us                                                | 5.05 us: 1.03x slower                                               |
| pickle_dict          | 27.6 us                                                | 31.3 us: 1.13x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.93 ms: 1.58x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.47 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.60 ms: 1.53x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                               |
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                               |
| genshi_xml      | 63.7 ms                                                | 47.3 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                               |
| logging_silent          | 176 ns                                                 | 91.9 ns: 1.92x faster                                               |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                |
| asyncio_tcp             | 914 ms                                                 | 496 ms: 1.84x faster                                                |
| richards                | 75.2 ms                                                | 42.0 ms: 1.79x faster                                               |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                |
| chaos                   | 106 ms                                                 | 63.7 ms: 1.66x faster                                               |
| pyflate                 | 676 ms                                                 | 416 ms: 1.62x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 66.8 ms: 1.62x faster                                               |
| raytrace                | 467 ms                                                 | 289 ms: 1.61x faster                                                |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                                |
| hexiom                  | 9.43 ms                                                | 5.96 ms: 1.58x faster                                               |
| python_startup          | 14.1 ms                                                | 8.93 ms: 1.58x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 76.0 ms: 1.53x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.53x faster                                                |
| mako                    | 14.7 ms                                                | 9.60 ms: 1.53x faster                                               |
| spectral_norm           | 150 ms                                                 | 98.2 ms: 1.52x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                               |
| nbody                   | 144 ms                                                 | 95.8 ms: 1.50x faster                                               |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                |
| float                   | 109 ms                                                 | 73.2 ms: 1.49x faster                                               |
| chameleon               | 9.17 ms                                                | 6.28 ms: 1.46x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.44x faster                                              |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                               |
| html5lib                | 85.9 ms                                                | 60.0 ms: 1.43x faster                                               |
| json_dumps              | 13.4 ms                                                | 9.43 ms: 1.43x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 671 ms: 1.42x faster                                                |
| logging_simple          | 8.10 us                                                | 5.73 us: 1.41x faster                                               |
| logging_format          | 8.85 us                                                | 6.32 us: 1.40x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.40x faster                                               |
| thrift                  | 1.03 ms                                                | 747 us: 1.38x faster                                                |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| tornado_http            | 128 ms                                                 | 93.7 ms: 1.37x faster                                               |
| scimark_fft             | 421 ms                                                 | 308 ms: 1.37x faster                                                |
| async_tree_none         | 711 ms                                                 | 522 ms: 1.36x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                               |
| unpack_sequence         | 59.4 ns                                                | 43.9 ns: 1.35x faster                                               |
| aiohttp                 | 1.34 ms                                                | 993 us: 1.35x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                               |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.35x faster                                              |
| genshi_xml              | 63.7 ms                                                | 47.3 ms: 1.35x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                              |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| deepcopy                | 438 us                                                 | 330 us: 1.32x faster                                                |
| fannkuch                | 488 ms                                                 | 369 ms: 1.32x faster                                                |
| async_tree_memoization  | 855 ms                                                 | 647 ms: 1.32x faster                                                |
| nqueens                 | 100 ms                                                 | 75.7 ms: 1.32x faster                                               |
| coroutines              | 31.6 ms                                                | 24.3 ms: 1.30x faster                                               |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 51.4 ms: 1.27x faster                                               |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                              |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed | 949 ms                                                 | 753 ms: 1.26x faster                                                |
| dulwich_log             | 75.8 ms                                                | 62.3 ms: 1.22x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 77.4 ms: 1.21x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                               |
| bench_thread_pool       | 946 us                                                 | 782 us: 1.21x faster                                                |
| async_generators        | 426 ms                                                 | 354 ms: 1.21x faster                                                |
| sympy_str               | 325 ms                                                 | 271 ms: 1.20x faster                                                |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                               |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                |
| sqlite_synth            | 2.92 us                                                | 2.54 us: 1.15x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.45 ms: 1.14x faster                                               |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                               |
| json                    | 5.35 ms                                                | 4.76 ms: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                                |
| pickle_list             | 4.72 us                                                | 4.23 us: 1.12x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                               |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                |
| unpickle                | 14.2 us                                                | 12.9 us: 1.09x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| mdp                     | 2.74 sec                                               | 2.57 sec: 1.07x faster                                              |
| telco                   | 6.73 ms                                                | 6.37 ms: 1.06x faster                                               |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                                |
| pidigits                | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| generators              | 76.4 ms                                                | 77.1 ms: 1.01x slower                                               |
| unpickle_list           | 4.92 us                                                | 5.05 us: 1.03x slower                                               |
| regex_effbot            | 3.19 ms                                                | 3.51 ms: 1.10x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.47 ms: 1.12x slower                                               |
| dask                    | 436 ms                                                 | 494 ms: 1.13x slower                                                |
| pickle_dict             | 27.6 us                                                | 31.3 us: 1.13x slower                                               |
| gc_traversal            | 3.53 ms                                                | 4.05 ms: 1.15x slower                                               |
| coverage                | 74.7 ms                                                | 96.4 ms: 1.29x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230203-3.12.0a4+-1d81198/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198.json: mypy
