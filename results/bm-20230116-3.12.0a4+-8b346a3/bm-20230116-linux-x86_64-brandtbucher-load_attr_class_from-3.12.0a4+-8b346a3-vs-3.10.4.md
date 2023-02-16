
# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_attr_class_from
- machine: linux-x86_64
- commit hash: 8b346a3
- commit date: 2023-01-16
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.33 ms: 1.45x faster                                                        |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                       |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.4 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.6 ms: 1.54x faster                                                        |
| float          | 109 ms                                                 | 71.8 ms: 1.52x faster                                                        |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                        |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                         |
| regex_effbot   | 3.19 ms                                                | 3.47 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 272 us: 1.66x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.28 ms: 1.45x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                        |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 78.4 ms: 1.20x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.10 us: 1.15x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                         |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                                        |
| unpickle_list        | 4.92 us                                                | 5.03 us: 1.02x slower                                                        |
| pickle_dict          | 27.6 us                                                | 30.5 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.93 ms: 1.58x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.46 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.58 ms: 1.53x faster                                                        |
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                        |
| django_template | 46.3 ms                                                | 32.3 ms: 1.44x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                        |
| logging_silent          | 176 ns                                                 | 93.6 ns: 1.89x faster                                                        |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                                         |
| asyncio_tcp             | 914 ms                                                 | 495 ms: 1.85x faster                                                         |
| richards                | 75.2 ms                                                | 42.3 ms: 1.78x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 62.1 ms: 1.75x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 67.2 ms: 1.74x faster                                                        |
| go                      | 226 ms                                                 | 133 ms: 1.69x faster                                                         |
| pyflate                 | 676 ms                                                 | 403 ms: 1.68x faster                                                         |
| pickle_pure_python      | 452 us                                                 | 272 us: 1.66x faster                                                         |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                         |
| chaos                   | 106 ms                                                 | 64.8 ms: 1.63x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.93 ms: 1.58x faster                                                        |
| hexiom                  | 9.43 ms                                                | 5.98 ms: 1.58x faster                                                        |
| spectral_norm           | 150 ms                                                 | 95.9 ms: 1.56x faster                                                        |
| nbody                   | 144 ms                                                 | 93.6 ms: 1.54x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                         |
| mako                    | 14.7 ms                                                | 9.58 ms: 1.53x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 34.0 us: 1.52x faster                                                        |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.52x faster                                                         |
| float                   | 109 ms                                                 | 71.8 ms: 1.52x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.33 ms: 1.45x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.28 ms: 1.45x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                                        |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.44x faster                                                        |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 41.6 ns: 1.43x faster                                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.42x faster                                                        |
| logging_simple          | 8.10 us                                                | 5.69 us: 1.42x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 679 ms: 1.40x faster                                                         |
| scimark_fft             | 421 ms                                                 | 300 ms: 1.40x faster                                                         |
| logging_format          | 8.85 us                                                | 6.31 us: 1.40x faster                                                        |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                         |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.97 ms: 1.37x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 629 ms: 1.36x faster                                                         |
| tornado_http            | 128 ms                                                 | 94.4 ms: 1.36x faster                                                        |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                         |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 994 us: 1.35x faster                                                         |
| deepcopy                | 438 us                                                 | 326 us: 1.34x faster                                                         |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.34x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                        |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                         |
| fannkuch                | 488 ms                                                 | 371 ms: 1.31x faster                                                         |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.29x faster                                                         |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.28x faster                                                        |
| nqueens                 | 100 ms                                                 | 78.0 ms: 1.28x faster                                                        |
| sqlglot_optimize        | 65.2 ms                                                | 50.9 ms: 1.28x faster                                                        |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 756 ms: 1.25x faster                                                         |
| coroutines              | 31.6 ms                                                | 25.3 ms: 1.25x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 774 us: 1.22x faster                                                         |
| async_generators        | 426 ms                                                 | 349 ms: 1.22x faster                                                         |
| dulwich_log             | 75.8 ms                                                | 62.5 ms: 1.21x faster                                                        |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                                        |
| sympy_str               | 325 ms                                                 | 269 ms: 1.21x faster                                                         |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 78.4 ms: 1.20x faster                                                        |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                         |
| json                    | 5.35 ms                                                | 4.57 ms: 1.17x faster                                                        |
| sympy_expand            | 534 ms                                                 | 456 ms: 1.17x faster                                                         |
| pickle_list             | 4.72 us                                                | 4.10 us: 1.15x faster                                                        |
| djangocms               | 36.9 us                                                | 32.1 us: 1.15x faster                                                        |
| sqlite_synth            | 2.92 us                                                | 2.57 us: 1.14x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.46 sec: 1.12x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                         |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                         |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                                        |
| telco                   | 6.73 ms                                                | 6.50 ms: 1.03x faster                                                        |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                         |
| generators              | 76.4 ms                                                | 77.2 ms: 1.01x slower                                                        |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                                         |
| unpickle_list           | 4.92 us                                                | 5.03 us: 1.02x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.47 ms: 1.09x slower                                                        |
| pickle_dict             | 27.6 us                                                | 30.5 us: 1.11x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.46 ms: 1.12x slower                                                        |
| dask                    | 436 ms                                                 | 501 ms: 1.15x slower                                                         |
| gc_traversal            | 3.53 ms                                                | 4.16 ms: 1.18x slower                                                        |
| coverage                | 74.7 ms                                                | 96.0 ms: 1.28x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230116-3.12.0a4+-8b346a3/bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3.json: mypy
