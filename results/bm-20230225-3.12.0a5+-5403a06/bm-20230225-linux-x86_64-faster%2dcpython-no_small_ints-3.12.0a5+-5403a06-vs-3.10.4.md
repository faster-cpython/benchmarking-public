
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_small_ints
- machine: linux-x86_64
- commit hash: 5403a06
- commit date: 2023-02-25
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.35x faster                                                      |
| chameleon      | 9.17 ms                                                | 6.46 ms: 1.42x faster                                                     |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                    |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                     |
| tornado_http   | 128 ms                                                 | 94.6 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 96.1 ms: 1.50x faster                                                     |
| float          | 109 ms                                                 | 74.9 ms: 1.45x faster                                                     |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                     |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                                      |
| regex_effbot   | 3.19 ms                                                | 3.69 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                                      |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                      |
| json_dumps           | 13.4 ms                                                | 9.28 ms: 1.45x faster                                                     |
| xml_etree_process    | 74.5 ms                                                | 55.0 ms: 1.36x faster                                                     |
| json_loads           | 28.7 us                                                | 23.5 us: 1.22x faster                                                     |
| xml_etree_generate   | 93.8 ms                                                | 80.6 ms: 1.16x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 99.2 ms: 1.12x faster                                                     |
| pickle_list          | 4.72 us                                                | 4.25 us: 1.11x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                      |
| unpickle             | 14.2 us                                                | 13.2 us: 1.08x faster                                                     |
| unpickle_list        | 4.92 us                                                | 4.97 us: 1.01x slower                                                     |
| pickle_dict          | 27.6 us                                                | 31.5 us: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                              |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.07 ms: 1.55x faster                                                     |
| python_startup_no_site | 5.78 ms                                                | 6.57 ms: 1.14x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.46x faster                                                     |
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                     |
| django_template | 46.3 ms                                                | 33.3 ms: 1.39x faster                                                     |
| genshi_xml      | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.8 ms: 2.48x faster                                                     |
| deltablue               | 7.28 ms                                                | 3.19 ms: 2.28x faster                                                     |
| logging_silent          | 176 ns                                                 | 93.4 ns: 1.89x faster                                                     |
| asyncio_tcp             | 914 ms                                                 | 500 ms: 1.83x faster                                                      |
| richards                | 75.2 ms                                                | 41.4 ms: 1.82x faster                                                     |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.77x faster                                                      |
| raytrace                | 467 ms                                                 | 282 ms: 1.65x faster                                                      |
| go                      | 226 ms                                                 | 139 ms: 1.62x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                                      |
| scimark_monte_carlo     | 109 ms                                                 | 68.7 ms: 1.58x faster                                                     |
| pyflate                 | 676 ms                                                 | 435 ms: 1.55x faster                                                      |
| python_startup          | 14.1 ms                                                | 9.07 ms: 1.55x faster                                                     |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                      |
| deepcopy_memo           | 51.7 us                                                | 33.9 us: 1.52x faster                                                     |
| hexiom                  | 9.43 ms                                                | 6.27 ms: 1.50x faster                                                     |
| nbody                   | 144 ms                                                 | 96.1 ms: 1.50x faster                                                     |
| chaos                   | 106 ms                                                 | 70.8 ms: 1.49x faster                                                     |
| crypto_pyaes            | 117 ms                                                 | 78.4 ms: 1.49x faster                                                     |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.48x faster                                                      |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.46x faster                                                     |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                     |
| float                   | 109 ms                                                 | 74.9 ms: 1.45x faster                                                     |
| json_dumps              | 13.4 ms                                                | 9.28 ms: 1.45x faster                                                     |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.42x faster                                                    |
| spectral_norm           | 150 ms                                                 | 105 ms: 1.42x faster                                                      |
| chameleon               | 9.17 ms                                                | 6.46 ms: 1.42x faster                                                     |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                                     |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.40x faster                                                     |
| pprint_safe_repr        | 953 ms                                                 | 681 ms: 1.40x faster                                                      |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                     |
| logging_simple          | 8.10 us                                                | 5.81 us: 1.39x faster                                                     |
| django_template         | 46.3 ms                                                | 33.3 ms: 1.39x faster                                                     |
| logging_format          | 8.85 us                                                | 6.37 us: 1.39x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                    |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.37x faster                                                    |
| async_tree_none         | 711 ms                                                 | 523 ms: 1.36x faster                                                      |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                      |
| genshi_xml              | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                     |
| xml_etree_process       | 74.5 ms                                                | 55.0 ms: 1.36x faster                                                     |
| tornado_http            | 128 ms                                                 | 94.6 ms: 1.36x faster                                                     |
| 2to3                    | 335 ms                                                 | 249 ms: 1.35x faster                                                      |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                     |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 44.7 ns: 1.33x faster                                                     |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                     |
| scimark_fft             | 421 ms                                                 | 321 ms: 1.31x faster                                                      |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                      |
| coroutines              | 31.6 ms                                                | 24.3 ms: 1.30x faster                                                     |
| mypy2                   | 430 ms                                                 | 331 ms: 1.30x faster                                                      |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                      |
| sqlglot_optimize        | 65.2 ms                                                | 50.5 ms: 1.29x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.29x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 743 ms: 1.28x faster                                                      |
| async_tree_memoization  | 855 ms                                                 | 670 ms: 1.28x faster                                                      |
| fannkuch                | 488 ms                                                 | 389 ms: 1.25x faster                                                      |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                    |
| json_loads              | 28.7 us                                                | 23.5 us: 1.22x faster                                                     |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                      |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                                     |
| nqueens                 | 100 ms                                                 | 82.9 ms: 1.21x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.52 ms: 1.21x faster                                                     |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.8 ms: 1.20x faster                                                     |
| bench_thread_pool       | 946 us                                                 | 787 us: 1.20x faster                                                      |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                                     |
| xml_etree_generate      | 93.8 ms                                                | 80.6 ms: 1.16x faster                                                     |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                     |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                     |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 99.2 ms: 1.12x faster                                                     |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                                     |
| pickle_list             | 4.72 us                                                | 4.25 us: 1.11x faster                                                     |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                      |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                                     |
| unpickle                | 14.2 us                                                | 13.2 us: 1.08x faster                                                     |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.65 sec: 1.04x faster                                                    |
| telco                   | 6.73 ms                                                | 6.52 ms: 1.03x faster                                                     |
| async_generators        | 426 ms                                                 | 422 ms: 1.01x faster                                                      |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                      |
| unpickle_list           | 4.92 us                                                | 4.97 us: 1.01x slower                                                     |
| gc_traversal            | 3.53 ms                                                | 3.83 ms: 1.09x slower                                                     |
| python_startup_no_site  | 5.78 ms                                                | 6.57 ms: 1.14x slower                                                     |
| pickle_dict             | 27.6 us                                                | 31.5 us: 1.14x slower                                                     |
| regex_effbot            | 3.19 ms                                                | 3.69 ms: 1.16x slower                                                     |
| dask                    | 436 ms                                                 | 506 ms: 1.16x slower                                                      |
| coverage                | 74.7 ms                                                | 99.6 ms: 1.33x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                              |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
