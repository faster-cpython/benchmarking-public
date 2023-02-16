
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1134727
- commit date: 2023-02-08
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| chameleon      | 9.17 ms                                                | 6.30 ms: 1.46x faster                                               |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                              |
| html5lib       | 85.9 ms                                                | 61.0 ms: 1.41x faster                                               |
| tornado_http   | 128 ms                                                 | 94.2 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 109 ms                                                 | 71.4 ms: 1.52x faster                                               |
| nbody          | 144 ms                                                 | 95.0 ms: 1.51x faster                                               |
| pidigits       | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.29x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                               |
| regex_dna      | 214 ms                                                 | 212 ms: 1.01x faster                                                |
| regex_effbot   | 3.19 ms                                                | 3.46 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 288 us: 1.57x faster                                                |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.60 ms: 1.40x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 55.1 ms: 1.35x faster                                               |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 80.4 ms: 1.17x faster                                               |
| pickle_list          | 4.72 us                                                | 4.22 us: 1.12x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| unpickle_list        | 4.92 us                                                | 4.89 us: 1.01x faster                                               |
| pickle_dict          | 27.6 us                                                | 32.0 us: 1.16x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.92 ms: 1.58x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.48 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.62 ms: 1.52x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                               |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                               |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                               |
| logging_silent          | 176 ns                                                 | 91.8 ns: 1.92x faster                                               |
| asyncio_tcp             | 914 ms                                                 | 492 ms: 1.86x faster                                                |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                |
| richards                | 75.2 ms                                                | 42.4 ms: 1.77x faster                                               |
| pyflate                 | 676 ms                                                 | 402 ms: 1.68x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 64.6 ms: 1.68x faster                                               |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                |
| raytrace                | 467 ms                                                 | 285 ms: 1.63x faster                                                |
| chaos                   | 106 ms                                                 | 65.7 ms: 1.61x faster                                               |
| hexiom                  | 9.43 ms                                                | 5.96 ms: 1.58x faster                                               |
| python_startup          | 14.1 ms                                                | 8.92 ms: 1.58x faster                                               |
| pickle_pure_python      | 452 us                                                 | 288 us: 1.57x faster                                                |
| spectral_norm           | 150 ms                                                 | 95.2 ms: 1.57x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                |
| float                   | 109 ms                                                 | 71.4 ms: 1.52x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 76.5 ms: 1.52x faster                                               |
| mako                    | 14.7 ms                                                | 9.62 ms: 1.52x faster                                               |
| nbody                   | 144 ms                                                 | 95.0 ms: 1.51x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                               |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                |
| chameleon               | 9.17 ms                                                | 6.30 ms: 1.46x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.81 ms: 1.43x faster                                               |
| scimark_fft             | 421 ms                                                 | 296 ms: 1.42x faster                                                |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                               |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                               |
| html5lib                | 85.9 ms                                                | 61.0 ms: 1.41x faster                                               |
| unpack_sequence         | 59.4 ns                                                | 42.2 ns: 1.41x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 680 ms: 1.40x faster                                                |
| json_dumps              | 13.4 ms                                                | 9.60 ms: 1.40x faster                                               |
| logging_format          | 8.85 us                                                | 6.35 us: 1.39x faster                                               |
| logging_simple          | 8.10 us                                                | 5.82 us: 1.39x faster                                               |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                |
| thrift                  | 1.03 ms                                                | 755 us: 1.37x faster                                                |
| tornado_http            | 128 ms                                                 | 94.2 ms: 1.36x faster                                               |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 55.1 ms: 1.35x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                              |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.35x faster                                              |
| async_tree_none         | 711 ms                                                 | 530 ms: 1.34x faster                                                |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                               |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                               |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| deepcopy                | 438 us                                                 | 334 us: 1.31x faster                                                |
| mypy2                   | 430 ms                                                 | 330 ms: 1.30x faster                                                |
| async_tree_memoization  | 855 ms                                                 | 662 ms: 1.29x faster                                                |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                               |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.2 ms                                                | 51.2 ms: 1.27x faster                                               |
| nqueens                 | 100 ms                                                 | 79.1 ms: 1.27x faster                                               |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 761 ms: 1.25x faster                                                |
| coroutines              | 31.6 ms                                                | 25.9 ms: 1.22x faster                                               |
| dulwich_log             | 75.8 ms                                                | 62.3 ms: 1.22x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.22x faster                                               |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.7 ms: 1.21x faster                                               |
| bench_thread_pool       | 946 us                                                 | 785 us: 1.21x faster                                                |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                               |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                |
| xml_etree_generate      | 93.8 ms                                                | 80.4 ms: 1.17x faster                                               |
| sympy_sum               | 183 ms                                                 | 157 ms: 1.17x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                               |
| json                    | 5.35 ms                                                | 4.63 ms: 1.15x faster                                               |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                               |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                               |
| pickle_list             | 4.72 us                                                | 4.22 us: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| meteor_contest          | 114 ms                                                 | 108 ms: 1.06x faster                                                |
| mdp                     | 2.74 sec                                               | 2.60 sec: 1.05x faster                                              |
| telco                   | 6.73 ms                                                | 6.50 ms: 1.04x faster                                               |
| regex_dna               | 214 ms                                                 | 212 ms: 1.01x faster                                                |
| unpickle_list           | 4.92 us                                                | 4.89 us: 1.01x faster                                               |
| async_generators        | 426 ms                                                 | 424 ms: 1.01x faster                                                |
| gc_traversal            | 3.53 ms                                                | 3.52 ms: 1.00x faster                                               |
| generators              | 76.4 ms                                                | 79.4 ms: 1.04x slower                                               |
| pidigits                | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| regex_effbot            | 3.19 ms                                                | 3.46 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.48 ms: 1.12x slower                                               |
| pickle_dict             | 27.6 us                                                | 32.0 us: 1.16x slower                                               |
| coverage                | 74.7 ms                                                | 98.0 ms: 1.31x slower                                               |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
