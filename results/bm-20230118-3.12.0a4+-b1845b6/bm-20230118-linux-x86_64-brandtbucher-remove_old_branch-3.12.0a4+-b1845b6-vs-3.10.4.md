
# Results vs. 3.10.4

- fork: brandtbucher
- ref: remove_old_branch
- machine: linux-x86_64
- commit hash: b1845b6
- commit date: 2023-01-18
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.33x faster                                                      |
| chameleon      | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                     |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                    |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                     |
| tornado_http   | 128 ms                                                 | 93.4 ms: 1.37x faster                                                     |
| Geometric mean | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.8 ms: 1.55x faster                                                     |
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                                     |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                     |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                      |
| regex_effbot   | 3.19 ms                                                | 3.64 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.59x faster                                                      |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                      |
| json_dumps           | 13.4 ms                                                | 9.42 ms: 1.43x faster                                                     |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                     |
| xml_etree_generate   | 93.8 ms                                                | 77.9 ms: 1.20x faster                                                     |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                     |
| pickle_list          | 4.72 us                                                | 4.27 us: 1.10x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                      |
| unpickle             | 14.2 us                                                | 13.4 us: 1.06x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                      |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                                     |
| unpickle_list        | 4.92 us                                                | 5.01 us: 1.02x slower                                                     |
| pickle_dict          | 27.6 us                                                | 31.9 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                     |
| python_startup_no_site | 5.78 ms                                                | 6.48 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.70 ms: 1.51x faster                                                     |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                     |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                                     |
| genshi_xml      | 63.7 ms                                                | 47.0 ms: 1.35x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                                     |
| logging_silent          | 176 ns                                                 | 91.6 ns: 1.93x faster                                                     |
| asyncio_tcp             | 914 ms                                                 | 489 ms: 1.87x faster                                                      |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                      |
| richards                | 75.2 ms                                                | 42.1 ms: 1.79x faster                                                     |
| pyflate                 | 676 ms                                                 | 397 ms: 1.70x faster                                                      |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                                      |
| scimark_monte_carlo     | 109 ms                                                 | 65.1 ms: 1.67x faster                                                     |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                      |
| chaos                   | 106 ms                                                 | 64.3 ms: 1.64x faster                                                     |
| crypto_pyaes            | 117 ms                                                 | 72.6 ms: 1.61x faster                                                     |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.59x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.96 ms: 1.57x faster                                                     |
| hexiom                  | 9.43 ms                                                | 6.02 ms: 1.57x faster                                                     |
| nbody                   | 144 ms                                                 | 92.8 ms: 1.55x faster                                                     |
| spectral_norm           | 150 ms                                                 | 97.6 ms: 1.53x faster                                                     |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                      |
| deepcopy_memo           | 51.7 us                                                | 33.9 us: 1.52x faster                                                     |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.51x faster                                                      |
| mako                    | 14.7 ms                                                | 9.70 ms: 1.51x faster                                                     |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                                     |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                     |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                                     |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                     |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                                     |
| chameleon               | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                     |
| json_dumps              | 13.4 ms                                                | 9.42 ms: 1.43x faster                                                     |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.42x faster                                                     |
| unpack_sequence         | 59.4 ns                                                | 41.7 ns: 1.42x faster                                                     |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                                    |
| pprint_safe_repr        | 953 ms                                                 | 676 ms: 1.41x faster                                                      |
| logging_simple          | 8.10 us                                                | 5.76 us: 1.41x faster                                                     |
| thrift                  | 1.03 ms                                                | 738 us: 1.40x faster                                                      |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                      |
| logging_format          | 8.85 us                                                | 6.36 us: 1.39x faster                                                     |
| scimark_fft             | 421 ms                                                 | 303 ms: 1.39x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                     |
| tornado_http            | 128 ms                                                 | 93.4 ms: 1.37x faster                                                     |
| async_tree_memoization  | 855 ms                                                 | 625 ms: 1.37x faster                                                      |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                      |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                                    |
| genshi_xml              | 63.7 ms                                                | 47.0 ms: 1.35x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                                     |
| fannkuch                | 488 ms                                                 | 362 ms: 1.35x faster                                                      |
| aiohttp                 | 1.34 ms                                                | 996 us: 1.35x faster                                                      |
| deepcopy                | 438 us                                                 | 326 us: 1.34x faster                                                      |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.34x faster                                                    |
| 2to3                    | 335 ms                                                 | 251 ms: 1.33x faster                                                      |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                                     |
| nqueens                 | 100 ms                                                 | 76.7 ms: 1.31x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 2.91 us: 1.30x faster                                                     |
| sqlglot_optimize        | 65.2 ms                                                | 50.9 ms: 1.28x faster                                                     |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                      |
| coroutines              | 31.6 ms                                                | 24.8 ms: 1.27x faster                                                     |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                    |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 19.6 ms: 1.22x faster                                                     |
| dulwich_log             | 75.8 ms                                                | 62.0 ms: 1.22x faster                                                     |
| bench_thread_pool       | 946 us                                                 | 774 us: 1.22x faster                                                      |
| sympy_str               | 325 ms                                                 | 268 ms: 1.21x faster                                                      |
| xml_etree_generate      | 93.8 ms                                                | 77.9 ms: 1.20x faster                                                     |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                     |
| async_generators        | 426 ms                                                 | 355 ms: 1.20x faster                                                      |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.19x faster                                                      |
| sympy_expand            | 534 ms                                                 | 451 ms: 1.18x faster                                                      |
| json                    | 5.35 ms                                                | 4.59 ms: 1.17x faster                                                     |
| djangocms               | 36.9 us                                                | 32.7 us: 1.13x faster                                                     |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                     |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                     |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.11x faster                                                     |
| pickle_list             | 4.72 us                                                | 4.27 us: 1.10x faster                                                     |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                                     |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                      |
| telco                   | 6.73 ms                                                | 6.26 ms: 1.08x faster                                                     |
| unpickle                | 14.2 us                                                | 13.4 us: 1.06x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                      |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                    |
| generators              | 76.4 ms                                                | 76.9 ms: 1.01x slower                                                     |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                                     |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                      |
| unpickle_list           | 4.92 us                                                | 5.01 us: 1.02x slower                                                     |
| python_startup_no_site  | 5.78 ms                                                | 6.48 ms: 1.12x slower                                                     |
| dask                    | 436 ms                                                 | 495 ms: 1.14x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.64 ms: 1.14x slower                                                     |
| pickle_dict             | 27.6 us                                                | 31.9 us: 1.16x slower                                                     |
| gc_traversal            | 3.53 ms                                                | 4.30 ms: 1.22x slower                                                     |
| coverage                | 74.7 ms                                                | 97.0 ms: 1.30x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-b1845b6/bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6.json: mypy
