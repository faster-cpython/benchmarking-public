
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 5a2b984
- commit date: 2023-02-04
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.33x faster                                   |
| chameleon      | 9.17 ms                                                | 6.29 ms: 1.46x faster                                  |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 60.0 ms: 1.43x faster                                  |
| tornado_http   | 128 ms                                                 | 94.1 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.8 ms: 1.53x faster                                  |
| float          | 109 ms                                                 | 72.8 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                  |
| regex_dna      | 214 ms                                                 | 216 ms: 1.01x slower                                   |
| regex_effbot   | 3.19 ms                                                | 3.64 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                   |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.26 ms: 1.45x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 77.3 ms: 1.21x faster                                  |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| pickle_list          | 4.72 us                                                | 4.05 us: 1.17x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                  |
| unpickle_list        | 4.92 us                                                | 5.02 us: 1.02x slower                                  |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.93 ms: 1.58x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.46 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.70 ms: 1.51x faster                                  |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.49x faster                                  |
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                  |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                  |
| logging_silent          | 176 ns                                                 | 92.8 ns: 1.90x faster                                  |
| asyncio_tcp             | 914 ms                                                 | 494 ms: 1.85x faster                                   |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                   |
| richards                | 75.2 ms                                                | 43.2 ms: 1.74x faster                                  |
| pyflate                 | 676 ms                                                 | 405 ms: 1.67x faster                                   |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                   |
| spectral_norm           | 150 ms                                                 | 91.5 ms: 1.63x faster                                  |
| chaos                   | 106 ms                                                 | 64.7 ms: 1.63x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 66.8 ms: 1.63x faster                                  |
| raytrace                | 467 ms                                                 | 288 ms: 1.62x faster                                   |
| crypto_pyaes            | 117 ms                                                 | 72.3 ms: 1.61x faster                                  |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                   |
| python_startup          | 14.1 ms                                                | 8.93 ms: 1.58x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.01 ms: 1.57x faster                                  |
| nbody                   | 144 ms                                                 | 93.8 ms: 1.53x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                   |
| deepcopy_memo           | 51.7 us                                                | 34.1 us: 1.51x faster                                  |
| mako                    | 14.7 ms                                                | 9.70 ms: 1.51x faster                                  |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                   |
| float                   | 109 ms                                                 | 72.8 ms: 1.50x faster                                  |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.49x faster                                  |
| chameleon               | 9.17 ms                                                | 6.29 ms: 1.46x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.26 ms: 1.45x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                 |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                  |
| html5lib                | 85.9 ms                                                | 60.0 ms: 1.43x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 668 ms: 1.43x faster                                   |
| logging_simple          | 8.10 us                                                | 5.70 us: 1.42x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                  |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                  |
| logging_format          | 8.85 us                                                | 6.28 us: 1.41x faster                                  |
| scimark_fft             | 421 ms                                                 | 299 ms: 1.41x faster                                   |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 42.7 ns: 1.39x faster                                  |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                   |
| thrift                  | 1.03 ms                                                | 747 us: 1.38x faster                                   |
| tornado_http            | 128 ms                                                 | 94.1 ms: 1.36x faster                                  |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                   |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                 |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.34x faster                                 |
| aiohttp                 | 1.34 ms                                                | 999 us: 1.34x faster                                   |
| deepcopy                | 438 us                                                 | 327 us: 1.34x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                  |
| fannkuch                | 488 ms                                                 | 368 ms: 1.33x faster                                   |
| 2to3                    | 335 ms                                                 | 253 ms: 1.33x faster                                   |
| async_tree_memoization  | 855 ms                                                 | 655 ms: 1.30x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.20 ms: 1.30x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.7 ms: 1.29x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.97 us: 1.28x faster                                  |
| coroutines              | 31.6 ms                                                | 24.9 ms: 1.27x faster                                  |
| nqueens                 | 100 ms                                                 | 78.8 ms: 1.27x faster                                  |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                 |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                   |
| async_generators        | 426 ms                                                 | 349 ms: 1.22x faster                                   |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.22x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 77.3 ms: 1.21x faster                                  |
| bench_thread_pool       | 946 us                                                 | 785 us: 1.20x faster                                   |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| dulwich_log             | 75.8 ms                                                | 63.2 ms: 1.20x faster                                  |
| sympy_str               | 325 ms                                                 | 272 ms: 1.19x faster                                   |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                   |
| json                    | 5.35 ms                                                | 4.57 ms: 1.17x faster                                  |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                   |
| pickle_list             | 4.72 us                                                | 4.05 us: 1.17x faster                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                  |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.11x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                  |
| mdp                     | 2.74 sec                                               | 2.53 sec: 1.08x faster                                 |
| meteor_contest          | 114 ms                                                 | 107 ms: 1.06x faster                                   |
| telco                   | 6.73 ms                                                | 6.35 ms: 1.06x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| generators              | 76.4 ms                                                | 76.8 ms: 1.00x slower                                  |
| regex_dna               | 214 ms                                                 | 216 ms: 1.01x slower                                   |
| unpickle_list           | 4.92 us                                                | 5.02 us: 1.02x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.65 ms: 1.04x slower                                  |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.46 ms: 1.12x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.64 ms: 1.14x slower                                  |
| dask                    | 436 ms                                                 | 501 ms: 1.15x slower                                   |
| coverage                | 74.7 ms                                                | 96.2 ms: 1.29x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230204-3.12.0a4+-5a2b984/bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984.json: mypy
