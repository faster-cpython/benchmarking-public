
# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_superinstructions
- machine: linux-x86_64
- commit hash: b633237
- commit date: 2023-01-14
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 255 ms: 1.31x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.49 ms: 1.41x faster                                                        |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                       |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.9 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.2 ms: 1.53x faster                                                        |
| float          | 109 ms                                                 | 72.2 ms: 1.51x faster                                                        |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                        |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                         |
| regex_effbot   | 3.19 ms                                                | 3.54 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.38 ms: 1.43x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 77.0 ms: 1.22x faster                                                        |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.02 us: 1.18x faster                                                        |
| unpickle             | 14.2 us                                                | 12.9 us: 1.10x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.05x faster                                                         |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                                        |
| pickle_dict          | 27.6 us                                                | 29.5 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.74 ms: 1.61x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.30 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.22x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                        |
| mako            | 14.7 ms                                                | 9.89 ms: 1.48x faster                                                        |
| django_template | 46.3 ms                                                | 32.7 ms: 1.41x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.23 ms: 2.26x faster                                                        |
| logging_silent          | 176 ns                                                 | 91.7 ns: 1.92x faster                                                        |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                         |
| asyncio_tcp             | 914 ms                                                 | 504 ms: 1.82x faster                                                         |
| richards                | 75.2 ms                                                | 44.0 ms: 1.71x faster                                                        |
| pyflate                 | 676 ms                                                 | 398 ms: 1.70x faster                                                         |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                 | 66.1 ms: 1.64x faster                                                        |
| raytrace                | 467 ms                                                 | 288 ms: 1.62x faster                                                         |
| python_startup          | 14.1 ms                                                | 8.74 ms: 1.61x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                                         |
| nbody                   | 144 ms                                                 | 94.2 ms: 1.53x faster                                                        |
| spectral_norm           | 150 ms                                                 | 98.0 ms: 1.53x faster                                                        |
| hexiom                  | 9.43 ms                                                | 6.18 ms: 1.53x faster                                                        |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.51x faster                                                         |
| float                   | 109 ms                                                 | 72.2 ms: 1.51x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                                         |
| crypto_pyaes            | 117 ms                                                 | 77.7 ms: 1.50x faster                                                        |
| chaos                   | 106 ms                                                 | 70.4 ms: 1.50x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                        |
| mako                    | 14.7 ms                                                | 9.89 ms: 1.48x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.38 ms: 1.43x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                                       |
| deepcopy_memo           | 51.7 us                                                | 36.1 us: 1.43x faster                                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.42x faster                                                        |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                        |
| django_template         | 46.3 ms                                                | 32.7 ms: 1.41x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.49 ms: 1.41x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 676 ms: 1.41x faster                                                         |
| logging_simple          | 8.10 us                                                | 5.82 us: 1.39x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.38x faster                                                       |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                                         |
| logging_format          | 8.85 us                                                | 6.52 us: 1.36x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                                        |
| tornado_http            | 128 ms                                                 | 94.9 ms: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                       |
| async_tree_none         | 711 ms                                                 | 530 ms: 1.34x faster                                                         |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                         |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                                        |
| scimark_fft             | 421 ms                                                 | 317 ms: 1.33x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.13 ms: 1.32x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                        |
| 2to3                    | 335 ms                                                 | 255 ms: 1.31x faster                                                         |
| fannkuch                | 488 ms                                                 | 374 ms: 1.30x faster                                                         |
| deepcopy                | 438 us                                                 | 336 us: 1.30x faster                                                         |
| async_tree_memoization  | 855 ms                                                 | 658 ms: 1.30x faster                                                         |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.28x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                         |
| sqlglot_optimize        | 65.2 ms                                                | 51.4 ms: 1.27x faster                                                        |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 749 ms: 1.27x faster                                                         |
| coroutines              | 31.6 ms                                                | 25.0 ms: 1.26x faster                                                        |
| nqueens                 | 100 ms                                                 | 79.4 ms: 1.26x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 77.0 ms: 1.22x faster                                                        |
| dulwich_log             | 75.8 ms                                                | 62.4 ms: 1.22x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 49.0 ns: 1.21x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 784 us: 1.21x faster                                                         |
| async_generators        | 426 ms                                                 | 356 ms: 1.20x faster                                                         |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                        |
| pickle_list             | 4.72 us                                                | 4.02 us: 1.18x faster                                                        |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.44 ms: 1.15x faster                                                        |
| sympy_expand            | 534 ms                                                 | 466 ms: 1.15x faster                                                         |
| json                    | 5.35 ms                                                | 4.71 ms: 1.14x faster                                                        |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                        |
| sympy_str               | 325 ms                                                 | 288 ms: 1.13x faster                                                         |
| djangocms               | 36.9 us                                                | 32.9 us: 1.12x faster                                                        |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                                         |
| unpickle                | 14.2 us                                                | 12.9 us: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                         |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.05x faster                                                         |
| mdp                     | 2.74 sec                                               | 2.61 sec: 1.05x faster                                                       |
| telco                   | 6.73 ms                                                | 6.43 ms: 1.05x faster                                                        |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                         |
| generators              | 76.4 ms                                                | 74.6 ms: 1.02x faster                                                        |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                                        |
| gc_traversal            | 3.53 ms                                                | 3.50 ms: 1.01x faster                                                        |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                                         |
| pickle_dict             | 27.6 us                                                | 29.5 us: 1.07x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.30 ms: 1.09x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.54 ms: 1.11x slower                                                        |
| dask                    | 436 ms                                                 | 507 ms: 1.16x slower                                                         |
| coverage                | 74.7 ms                                                | 96.2 ms: 1.29x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230114-3.12.0a4+-b633237/bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237.json: mypy
