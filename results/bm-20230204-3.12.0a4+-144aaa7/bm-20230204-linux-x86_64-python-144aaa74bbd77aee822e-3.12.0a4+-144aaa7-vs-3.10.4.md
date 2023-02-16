
# Results vs. 3.10.4

- fork: python
- ref: 144aaa74bbd77aee822e
- machine: linux-x86_64
- commit hash: 144aaa7
- commit date: 2023-02-04
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.33x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.25 ms: 1.47x faster                                                  |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                 |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                  |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 109 ms                                                 | 72.4 ms: 1.50x faster                                                  |
| nbody          | 144 ms                                                 | 97.5 ms: 1.48x faster                                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 126 ms: 1.41x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                  |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.63 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 281 us: 1.61x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.48 ms: 1.42x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 77.4 ms: 1.21x faster                                                  |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.24 us: 1.11x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                                   |
| unpickle_list        | 4.92 us                                                | 5.12 us: 1.04x slower                                                  |
| unpickle             | 14.2 us                                                | 14.9 us: 1.05x slower                                                  |
| pickle_dict          | 27.6 us                                                | 31.9 us: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.93 ms: 1.58x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.46 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.79 ms: 1.50x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                  |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                  |
| logging_silent          | 176 ns                                                 | 92.3 ns: 1.91x faster                                                  |
| asyncio_tcp             | 914 ms                                                 | 491 ms: 1.86x faster                                                   |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                                   |
| richards                | 75.2 ms                                                | 42.3 ms: 1.78x faster                                                  |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                   |
| pyflate                 | 676 ms                                                 | 404 ms: 1.67x faster                                                   |
| raytrace                | 467 ms                                                 | 282 ms: 1.65x faster                                                   |
| chaos                   | 106 ms                                                 | 65.0 ms: 1.63x faster                                                  |
| crypto_pyaes            | 117 ms                                                 | 72.1 ms: 1.62x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                 | 67.2 ms: 1.61x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 281 us: 1.61x faster                                                   |
| python_startup          | 14.1 ms                                                | 8.93 ms: 1.58x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.05 ms: 1.56x faster                                                  |
| spectral_norm           | 150 ms                                                 | 97.2 ms: 1.54x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                   |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                                  |
| float                   | 109 ms                                                 | 72.4 ms: 1.50x faster                                                  |
| mako                    | 14.7 ms                                                | 9.79 ms: 1.50x faster                                                  |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                  |
| nbody                   | 144 ms                                                 | 97.5 ms: 1.48x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.25 ms: 1.47x faster                                                  |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                   |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                                 |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                  |
| unpack_sequence         | 59.4 ns                                                | 41.7 ns: 1.43x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 669 ms: 1.42x faster                                                   |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                  |
| logging_simple          | 8.10 us                                                | 5.71 us: 1.42x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.48 ms: 1.42x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                                  |
| logging_format          | 8.85 us                                                | 6.29 us: 1.41x faster                                                  |
| regex_compile           | 177 ms                                                 | 126 ms: 1.41x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                  |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                                  |
| thrift                  | 1.03 ms                                                | 758 us: 1.36x faster                                                   |
| scimark_fft             | 421 ms                                                 | 310 ms: 1.36x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                  |
| deepcopy                | 438 us                                                 | 323 us: 1.35x faster                                                   |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                 |
| fannkuch                | 488 ms                                                 | 363 ms: 1.34x faster                                                   |
| aiohttp                 | 1.34 ms                                                | 997 us: 1.34x faster                                                   |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.34x faster                                                 |
| 2to3                    | 335 ms                                                 | 253 ms: 1.33x faster                                                   |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                                  |
| async_tree_memoization  | 855 ms                                                 | 652 ms: 1.31x faster                                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.28x faster                                                  |
| nqueens                 | 100 ms                                                 | 78.3 ms: 1.28x faster                                                  |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                 |
| async_tree_cpu_io_mixed | 949 ms                                                 | 760 ms: 1.25x faster                                                   |
| coroutines              | 31.6 ms                                                | 25.7 ms: 1.23x faster                                                  |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                                  |
| xml_etree_generate      | 93.8 ms                                                | 77.4 ms: 1.21x faster                                                  |
| async_generators        | 426 ms                                                 | 352 ms: 1.21x faster                                                   |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 785 us: 1.21x faster                                                   |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                   |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                  |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                   |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                   |
| djangocms               | 36.9 us                                                | 32.2 us: 1.14x faster                                                  |
| json                    | 5.35 ms                                                | 4.72 ms: 1.13x faster                                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.13x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                  |
| pickle_list             | 4.72 us                                                | 4.24 us: 1.11x faster                                                  |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                                   |
| mdp                     | 2.74 sec                                               | 2.61 sec: 1.05x faster                                                 |
| telco                   | 6.73 ms                                                | 6.55 ms: 1.03x faster                                                  |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                   |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                                   |
| gc_traversal            | 3.53 ms                                                | 3.65 ms: 1.04x slower                                                  |
| unpickle_list           | 4.92 us                                                | 5.12 us: 1.04x slower                                                  |
| unpickle                | 14.2 us                                                | 14.9 us: 1.05x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.46 ms: 1.12x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.63 ms: 1.14x slower                                                  |
| dask                    | 436 ms                                                 | 497 ms: 1.14x slower                                                   |
| pickle_dict             | 27.6 us                                                | 31.9 us: 1.16x slower                                                  |
| coverage                | 74.7 ms                                                | 94.5 ms: 1.26x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (3): pickle, bench_mp_pool, generators
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230204-3.12.0a4+-144aaa7/bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7.json: mypy
