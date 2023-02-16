
# Results vs. 3.10.4

- fork: DinoV
- ref: coro_freelist
- machine: linux-x86_64
- commit hash: a371554
- commit date: 2023-01-19
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                           |
| chameleon      | 9.17 ms                                                | 6.31 ms: 1.45x faster                                          |
| docutils       | 3.18 sec                                               | 2.47 sec: 1.28x faster                                         |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                          |
| tornado_http   | 128 ms                                                 | 93.7 ms: 1.37x faster                                          |
| Geometric mean | (ref)                                                  | 1.38x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.2 ms: 1.53x faster                                          |
| float          | 109 ms                                                 | 71.7 ms: 1.52x faster                                          |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.32x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                           |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                          |
| regex_dna      | 214 ms                                                 | 201 ms: 1.07x faster                                           |
| regex_effbot   | 3.19 ms                                                | 3.36 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                  | 1.13x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                           |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                           |
| json_dumps           | 13.4 ms                                                | 9.39 ms: 1.43x faster                                          |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                          |
| xml_etree_generate   | 93.8 ms                                                | 77.1 ms: 1.22x faster                                          |
| json_loads           | 28.7 us                                                | 24.0 us: 1.19x faster                                          |
| pickle_list          | 4.72 us                                                | 4.03 us: 1.17x faster                                          |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                           |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                           |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                          |
| unpickle_list        | 4.92 us                                                | 4.96 us: 1.01x slower                                          |
| pickle_dict          | 27.6 us                                                | 29.7 us: 1.08x slower                                          |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                   |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.86 ms: 1.59x faster                                          |
| python_startup_no_site | 5.78 ms                                                | 6.42 ms: 1.11x slower                                          |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.59 ms: 1.53x faster                                          |
| genshi_text     | 30.6 ms                                                | 21.4 ms: 1.43x faster                                          |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                          |
| genshi_xml      | 63.7 ms                                                | 47.3 ms: 1.35x faster                                          |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                   |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.28x faster                                          |
| logging_silent          | 176 ns                                                 | 91.6 ns: 1.93x faster                                          |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                           |
| asyncio_tcp             | 914 ms                                                 | 501 ms: 1.83x faster                                           |
| richards                | 75.2 ms                                                | 42.2 ms: 1.78x faster                                          |
| pyflate                 | 676 ms                                                 | 402 ms: 1.68x faster                                           |
| scimark_monte_carlo     | 109 ms                                                 | 65.8 ms: 1.65x faster                                          |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                           |
| go                      | 226 ms                                                 | 140 ms: 1.61x faster                                           |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                           |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.60x faster                                          |
| python_startup          | 14.1 ms                                                | 8.86 ms: 1.59x faster                                          |
| crypto_pyaes            | 117 ms                                                 | 74.5 ms: 1.57x faster                                          |
| hexiom                  | 9.43 ms                                                | 6.03 ms: 1.56x faster                                          |
| chaos                   | 106 ms                                                 | 67.9 ms: 1.56x faster                                          |
| deepcopy_memo           | 51.7 us                                                | 33.4 us: 1.55x faster                                          |
| mako                    | 14.7 ms                                                | 9.59 ms: 1.53x faster                                          |
| nbody                   | 144 ms                                                 | 94.2 ms: 1.53x faster                                          |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                           |
| float                   | 109 ms                                                 | 71.7 ms: 1.52x faster                                          |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                           |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.47x faster                                          |
| pprint_pformat          | 1.98 sec                                               | 1.36 sec: 1.45x faster                                         |
| chameleon               | 9.17 ms                                                | 6.31 ms: 1.45x faster                                          |
| sqlglot_transpile       | 2.43 ms                                                | 1.68 ms: 1.44x faster                                          |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                          |
| pprint_safe_repr        | 953 ms                                                 | 663 ms: 1.44x faster                                           |
| genshi_text             | 30.6 ms                                                | 21.4 ms: 1.43x faster                                          |
| json_dumps              | 13.4 ms                                                | 9.39 ms: 1.43x faster                                          |
| unpack_sequence         | 59.4 ns                                                | 41.5 ns: 1.43x faster                                          |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                          |
| pycparser               | 1.53 sec                                               | 1.08 sec: 1.41x faster                                         |
| logging_simple          | 8.10 us                                                | 5.74 us: 1.41x faster                                          |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                          |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                          |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                           |
| thrift                  | 1.03 ms                                                | 751 us: 1.38x faster                                           |
| tornado_http            | 128 ms                                                 | 93.7 ms: 1.37x faster                                          |
| coroutines              | 31.6 ms                                                | 23.2 ms: 1.36x faster                                          |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                           |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                          |
| aiohttp                 | 1.34 ms                                                | 993 us: 1.35x faster                                           |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                         |
| fannkuch                | 488 ms                                                 | 362 ms: 1.35x faster                                           |
| genshi_xml              | 63.7 ms                                                | 47.3 ms: 1.35x faster                                          |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.06 ms: 1.34x faster                                          |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                           |
| scimark_fft             | 421 ms                                                 | 314 ms: 1.34x faster                                           |
| deepcopy                | 438 us                                                 | 328 us: 1.33x faster                                           |
| async_tree_memoization  | 855 ms                                                 | 646 ms: 1.32x faster                                           |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.30x faster                                           |
| nqueens                 | 100 ms                                                 | 77.1 ms: 1.30x faster                                          |
| sqlglot_optimize        | 65.2 ms                                                | 50.6 ms: 1.29x faster                                          |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.29x faster                                          |
| docutils                | 3.18 sec                                               | 2.47 sec: 1.28x faster                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 746 ms: 1.27x faster                                           |
| dulwich_log             | 75.8 ms                                                | 62.0 ms: 1.22x faster                                          |
| xml_etree_generate      | 93.8 ms                                                | 77.1 ms: 1.22x faster                                          |
| bench_thread_pool       | 946 us                                                 | 783 us: 1.21x faster                                           |
| json_loads              | 28.7 us                                                | 24.0 us: 1.19x faster                                          |
| async_generators        | 426 ms                                                 | 357 ms: 1.19x faster                                           |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.19x faster                                          |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                          |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                           |
| pickle_list             | 4.72 us                                                | 4.03 us: 1.17x faster                                          |
| json                    | 5.35 ms                                                | 4.59 ms: 1.16x faster                                          |
| sympy_str               | 325 ms                                                 | 280 ms: 1.16x faster                                           |
| create_gc_cycles        | 1.65 ms                                                | 1.44 ms: 1.14x faster                                          |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                          |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                          |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                           |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                           |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                          |
| mdp                     | 2.74 sec                                               | 2.52 sec: 1.09x faster                                         |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                           |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                          |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.07x faster                                           |
| regex_dna               | 214 ms                                                 | 201 ms: 1.07x faster                                           |
| telco                   | 6.73 ms                                                | 6.33 ms: 1.06x faster                                          |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                           |
| generators              | 76.4 ms                                                | 76.7 ms: 1.00x slower                                          |
| unpickle_list           | 4.92 us                                                | 4.96 us: 1.01x slower                                          |
| regex_effbot            | 3.19 ms                                                | 3.36 ms: 1.05x slower                                          |
| pickle_dict             | 27.6 us                                                | 29.7 us: 1.08x slower                                          |
| python_startup_no_site  | 5.78 ms                                                | 6.42 ms: 1.11x slower                                          |
| dask                    | 436 ms                                                 | 495 ms: 1.14x slower                                           |
| gc_traversal            | 3.53 ms                                                | 4.29 ms: 1.22x slower                                          |
| coverage                | 74.7 ms                                                | 93.9 ms: 1.26x slower                                          |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                   |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230119-3.12.0a4+-a371554/bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554.json: mypy
