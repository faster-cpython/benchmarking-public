
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 53e50c4
- commit date: 2023-02-01
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 254 ms: 1.32x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.44 ms: 1.42x faster                                                        |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.1 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.7 ms: 1.54x faster                                                        |
| float          | 109 ms                                                 | 72.6 ms: 1.50x faster                                                        |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                        |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                         |
| regex_effbot   | 3.19 ms                                                | 3.52 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 288 us: 1.57x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 202 us: 1.49x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.62 ms: 1.40x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 77.7 ms: 1.21x faster                                                        |
| json_loads           | 28.7 us                                                | 24.0 us: 1.19x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.10 us: 1.15x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                                         |
| unpickle_list        | 4.92 us                                                | 4.96 us: 1.01x slower                                                        |
| pickle_dict          | 27.6 us                                                | 30.7 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.89 ms: 1.58x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.44 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.69 ms: 1.51x faster                                                        |
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                        |
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 46.6 ms: 1.37x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.26x faster                                                        |
| logging_silent          | 176 ns                                                 | 93.7 ns: 1.88x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 500 ms: 1.83x faster                                                         |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                         |
| richards                | 75.2 ms                                                | 42.1 ms: 1.79x faster                                                        |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                 | 65.0 ms: 1.67x faster                                                        |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                                         |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                                         |
| chaos                   | 106 ms                                                 | 65.0 ms: 1.62x faster                                                        |
| hexiom                  | 9.43 ms                                                | 5.89 ms: 1.60x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 72.9 ms: 1.60x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.89 ms: 1.58x faster                                                        |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.58x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 288 us: 1.57x faster                                                         |
| nbody                   | 144 ms                                                 | 93.7 ms: 1.54x faster                                                        |
| scimark_lu              | 161 ms                                                 | 105 ms: 1.53x faster                                                         |
| mako                    | 14.7 ms                                                | 9.69 ms: 1.51x faster                                                        |
| float                   | 109 ms                                                 | 72.6 ms: 1.50x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 202 us: 1.49x faster                                                         |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                       |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.44 ms: 1.42x faster                                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 675 ms: 1.41x faster                                                         |
| logging_simple          | 8.10 us                                                | 5.78 us: 1.40x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.62 ms: 1.40x faster                                                        |
| scimark_fft             | 421 ms                                                 | 302 ms: 1.39x faster                                                         |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                                         |
| logging_format          | 8.85 us                                                | 6.38 us: 1.39x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 46.6 ms: 1.37x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.00 ms: 1.36x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 43.6 ns: 1.36x faster                                                        |
| tornado_http            | 128 ms                                                 | 94.1 ms: 1.36x faster                                                        |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                         |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.35x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                       |
| fannkuch                | 488 ms                                                 | 364 ms: 1.34x faster                                                         |
| async_tree_none         | 711 ms                                                 | 530 ms: 1.34x faster                                                         |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                       |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                                         |
| 2to3                    | 335 ms                                                 | 254 ms: 1.32x faster                                                         |
| deepcopy_reduce         | 3.79 us                                                | 2.93 us: 1.29x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 666 ms: 1.28x faster                                                         |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                         |
| nqueens                 | 100 ms                                                 | 79.0 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 759 ms: 1.25x faster                                                         |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                       |
| coroutines              | 31.6 ms                                                | 25.5 ms: 1.24x faster                                                        |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 77.7 ms: 1.21x faster                                                        |
| async_generators        | 426 ms                                                 | 353 ms: 1.21x faster                                                         |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 787 us: 1.20x faster                                                         |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                         |
| json_loads              | 28.7 us                                                | 24.0 us: 1.19x faster                                                        |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                         |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.18x faster                                                         |
| pickle_list             | 4.72 us                                                | 4.10 us: 1.15x faster                                                        |
| sqlite_synth            | 2.92 us                                                | 2.57 us: 1.14x faster                                                        |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                                        |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                         |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.58 sec: 1.06x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                                         |
| telco                   | 6.73 ms                                                | 6.40 ms: 1.05x faster                                                        |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                         |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                         |
| unpickle_list           | 4.92 us                                                | 4.96 us: 1.01x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.52 ms: 1.10x slower                                                        |
| pickle_dict             | 27.6 us                                                | 30.7 us: 1.11x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.44 ms: 1.11x slower                                                        |
| dask                    | 436 ms                                                 | 497 ms: 1.14x slower                                                         |
| gc_traversal            | 3.53 ms                                                | 4.05 ms: 1.15x slower                                                        |
| coverage                | 74.7 ms                                                | 96.1 ms: 1.29x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (3): bench_mp_pool, generators, pickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-53e50c4/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4.json: mypy
