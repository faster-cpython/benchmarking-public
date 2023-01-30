
# Results vs. 3.10.4

- fork: DinoV
- ref: coro_freelist
- machine: linux-x86_64
- commit hash: a371554
- commit date: 2023-01-19
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 250 ms: 1.33x faster                                           |
| chameleon      | 8.86 ms                                                | 6.31 ms: 1.40x faster                                          |
| docutils       | 3.18 sec                                               | 2.47 sec: 1.29x faster                                         |
| html5lib       | 85.8 ms                                                | 59.7 ms: 1.44x faster                                          |
| tornado_http   | 128 ms                                                 | 93.7 ms: 1.37x faster                                          |
| Geometric mean | (ref)                                                  | 1.36x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.7 ms: 1.50x faster                                          |
| nbody          | 136 ms                                                 | 94.2 ms: 1.45x faster                                          |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.30x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                           |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                          |
| regex_dna      | 214 ms                                                 | 201 ms: 1.07x faster                                           |
| regex_effbot   | 3.21 ms                                                | 3.36 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                  | 1.13x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 282 us: 1.61x faster                                           |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                           |
| json_dumps           | 13.5 ms                                                | 9.39 ms: 1.44x faster                                          |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                          |
| xml_etree_generate   | 93.3 ms                                                | 77.1 ms: 1.21x faster                                          |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                          |
| pickle_list          | 4.50 us                                                | 4.03 us: 1.12x faster                                          |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                           |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                          |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                           |
| unpickle_list        | 4.99 us                                                | 4.96 us: 1.01x faster                                          |
| pickle_dict          | 28.3 us                                                | 29.7 us: 1.05x slower                                          |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                   |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.86 ms: 1.57x faster                                          |
| python_startup_no_site | 5.76 ms                                                | 6.42 ms: 1.11x slower                                          |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.59 ms: 1.49x faster                                          |
| genshi_text     | 30.6 ms                                                | 21.4 ms: 1.43x faster                                          |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                          |
| genshi_xml      | 63.6 ms                                                | 47.3 ms: 1.34x faster                                          |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                   |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.20 ms: 2.31x faster                                          |
| logging_silent          | 173 ns                                                 | 91.6 ns: 1.89x faster                                          |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                           |
| richards                | 71.4 ms                                                | 42.2 ms: 1.69x faster                                          |
| pyflate                 | 675 ms                                                 | 402 ms: 1.68x faster                                           |
| raytrace                | 461 ms                                                 | 283 ms: 1.63x faster                                           |
| go                      | 226 ms                                                 | 140 ms: 1.61x faster                                           |
| pickle_pure_python      | 453 us                                                 | 282 us: 1.61x faster                                           |
| scimark_monte_carlo     | 105 ms                                                 | 65.8 ms: 1.59x faster                                          |
| spectral_norm           | 148 ms                                                 | 93.8 ms: 1.58x faster                                          |
| crypto_pyaes            | 118 ms                                                 | 74.5 ms: 1.58x faster                                          |
| python_startup          | 13.9 ms                                                | 8.86 ms: 1.57x faster                                          |
| hexiom                  | 9.42 ms                                                | 6.03 ms: 1.56x faster                                          |
| chaos                   | 104 ms                                                 | 67.9 ms: 1.53x faster                                          |
| float                   | 108 ms                                                 | 71.7 ms: 1.50x faster                                          |
| deepcopy_memo           | 50.0 us                                                | 33.4 us: 1.50x faster                                          |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                           |
| mako                    | 14.3 ms                                                | 9.59 ms: 1.49x faster                                          |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.47x faster                                           |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.46x faster                                          |
| pprint_pformat          | 1.97 sec                                               | 1.36 sec: 1.45x faster                                         |
| nbody                   | 136 ms                                                 | 94.2 ms: 1.45x faster                                          |
| html5lib                | 85.8 ms                                                | 59.7 ms: 1.44x faster                                          |
| json_dumps              | 13.5 ms                                                | 9.39 ms: 1.44x faster                                          |
| sqlglot_transpile       | 2.42 ms                                                | 1.68 ms: 1.44x faster                                          |
| genshi_text             | 30.6 ms                                                | 21.4 ms: 1.43x faster                                          |
| unpack_sequence         | 59.5 ns                                                | 41.5 ns: 1.43x faster                                          |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                          |
| pprint_safe_repr        | 943 ms                                                 | 663 ms: 1.42x faster                                           |
| logging_format          | 8.92 us                                                | 6.34 us: 1.41x faster                                          |
| chameleon               | 8.86 ms                                                | 6.31 ms: 1.40x faster                                          |
| logging_simple          | 8.06 us                                                | 5.74 us: 1.40x faster                                          |
| pycparser               | 1.51 sec                                               | 1.08 sec: 1.40x faster                                         |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                          |
| thrift                  | 1.03 ms                                                | 751 us: 1.37x faster                                           |
| tornado_http            | 128 ms                                                 | 93.7 ms: 1.37x faster                                          |
| coroutines              | 31.7 ms                                                | 23.2 ms: 1.36x faster                                          |
| async_tree_none         | 713 ms                                                 | 526 ms: 1.35x faster                                           |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                          |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                           |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.06 ms: 1.35x faster                                          |
| aiohttp                 | 1.34 ms                                                | 993 us: 1.35x faster                                           |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                         |
| genshi_xml              | 63.6 ms                                                | 47.3 ms: 1.34x faster                                          |
| 2to3                    | 332 ms                                                 | 250 ms: 1.33x faster                                           |
| async_tree_memoization  | 854 ms                                                 | 646 ms: 1.32x faster                                           |
| scimark_fft             | 414 ms                                                 | 314 ms: 1.32x faster                                           |
| fannkuch                | 477 ms                                                 | 362 ms: 1.32x faster                                           |
| deepcopy                | 429 us                                                 | 328 us: 1.31x faster                                           |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                           |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                          |
| nqueens                 | 99.3 ms                                                | 77.1 ms: 1.29x faster                                          |
| docutils                | 3.18 sec                                               | 2.47 sec: 1.29x faster                                         |
| deepcopy_reduce         | 3.75 us                                                | 2.95 us: 1.27x faster                                          |
| async_tree_cpu_io_mixed | 949 ms                                                 | 746 ms: 1.27x faster                                           |
| mypy                    | 1.01 sec                                               | 810 ms: 1.25x faster                                           |
| dulwich_log             | 75.5 ms                                                | 62.0 ms: 1.22x faster                                          |
| xml_etree_generate      | 93.3 ms                                                | 77.1 ms: 1.21x faster                                          |
| bench_thread_pool       | 943 us                                                 | 783 us: 1.20x faster                                           |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                          |
| async_generators        | 428 ms                                                 | 357 ms: 1.20x faster                                           |
| sympy_expand            | 537 ms                                                 | 453 ms: 1.19x faster                                           |
| sympy_integrate         | 23.9 ms                                                | 20.3 ms: 1.18x faster                                          |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                          |
| json                    | 5.35 ms                                                | 4.59 ms: 1.17x faster                                          |
| sympy_str               | 324 ms                                                 | 280 ms: 1.16x faster                                           |
| sqlite_synth            | 2.90 us                                                | 2.56 us: 1.13x faster                                          |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                           |
| mdp                     | 2.82 sec                                               | 2.52 sec: 1.12x faster                                         |
| pickle_list             | 4.50 us                                                | 4.03 us: 1.12x faster                                          |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                           |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                          |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                          |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                           |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.07x faster                                           |
| regex_dna               | 214 ms                                                 | 201 ms: 1.07x faster                                           |
| telco                   | 6.68 ms                                                | 6.33 ms: 1.06x faster                                          |
| unpickle_list           | 4.99 us                                                | 4.96 us: 1.01x faster                                          |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                           |
| generators              | 75.8 ms                                                | 76.7 ms: 1.01x slower                                          |
| regex_effbot            | 3.21 ms                                                | 3.36 ms: 1.05x slower                                          |
| pickle_dict             | 28.3 us                                                | 29.7 us: 1.05x slower                                          |
| python_startup_no_site  | 5.76 ms                                                | 6.42 ms: 1.11x slower                                          |
| coverage                | 75.3 ms                                                | 93.9 ms: 1.25x slower                                          |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                   |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230119-3.12.0a4+-a371554/bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
