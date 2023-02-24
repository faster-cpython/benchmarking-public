
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 39ace64
- commit date: 2023-02-22
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.34x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.43 ms: 1.43x faster                                                        |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.24x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.5 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 96.7 ms: 1.49x faster                                                        |
| float          | 109 ms                                                 | 73.4 ms: 1.48x faster                                                        |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                        |
| regex_dna      | 214 ms                                                 | 216 ms: 1.01x slower                                                         |
| regex_effbot   | 3.19 ms                                                | 3.52 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.43 ms: 1.43x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 54.6 ms: 1.37x faster                                                        |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.03 us: 1.17x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 80.4 ms: 1.17x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 99.5 ms: 1.12x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.08x faster                                                         |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                                        |
| unpickle_list        | 4.92 us                                                | 5.02 us: 1.02x slower                                                        |
| pickle_dict          | 27.6 us                                                | 30.9 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.02 ms: 1.56x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.80 ms: 1.50x faster                                                        |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                        |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 46.7 ms: 1.36x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230222-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-39ace64 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.6 ms: 2.59x faster                                                        |
| deltablue               | 7.28 ms                                                | 3.14 ms: 2.32x faster                                                        |
| logging_silent          | 176 ns                                                 | 90.4 ns: 1.95x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 501 ms: 1.82x faster                                                         |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                                         |
| richards                | 75.2 ms                                                | 42.4 ms: 1.77x faster                                                        |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                         |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                                         |
| pyflate                 | 676 ms                                                 | 412 ms: 1.64x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                 | 66.2 ms: 1.64x faster                                                        |
| hexiom                  | 9.43 ms                                                | 5.90 ms: 1.60x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 73.1 ms: 1.59x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                                         |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.58x faster                                                        |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                                        |
| python_startup          | 14.1 ms                                                | 9.02 ms: 1.56x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                         |
| deepcopy_memo           | 51.7 us                                                | 34.1 us: 1.51x faster                                                        |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.51x faster                                                         |
| mako                    | 14.7 ms                                                | 9.80 ms: 1.50x faster                                                        |
| nbody                   | 144 ms                                                 | 96.7 ms: 1.49x faster                                                        |
| float                   | 109 ms                                                 | 73.4 ms: 1.48x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.47x faster                                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.68 ms: 1.44x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.43 ms: 1.43x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.43 ms: 1.43x faster                                                        |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                                       |
| coroutines              | 31.6 ms                                                | 22.4 ms: 1.41x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 42.4 ns: 1.40x faster                                                        |
| logging_simple          | 8.10 us                                                | 5.80 us: 1.40x faster                                                        |
| logging_format          | 8.85 us                                                | 6.36 us: 1.39x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 688 ms: 1.39x faster                                                         |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 54.6 ms: 1.37x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 46.7 ms: 1.36x faster                                                        |
| scimark_fft             | 421 ms                                                 | 309 ms: 1.36x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                       |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                                        |
| tornado_http            | 128 ms                                                 | 94.5 ms: 1.36x faster                                                        |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                                         |
| 2to3                    | 335 ms                                                 | 249 ms: 1.34x faster                                                         |
| fannkuch                | 488 ms                                                 | 364 ms: 1.34x faster                                                         |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                        |
| deepcopy                | 438 us                                                 | 330 us: 1.32x faster                                                         |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 102 ms: 1.32x faster                                                         |
| sqlglot_optimize        | 65.2 ms                                                | 50.2 ms: 1.30x faster                                                        |
| mypy2                   | 430 ms                                                 | 332 ms: 1.30x faster                                                         |
| deepcopy_reduce         | 3.79 us                                                | 2.93 us: 1.29x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 666 ms: 1.28x faster                                                         |
| nqueens                 | 100 ms                                                 | 78.1 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 744 ms: 1.28x faster                                                         |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.24x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                         |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.21x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 790 us: 1.20x faster                                                         |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                        |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.9 ms: 1.20x faster                                                        |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                        |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                         |
| pickle_list             | 4.72 us                                                | 4.03 us: 1.17x faster                                                        |
| json                    | 5.35 ms                                                | 4.58 ms: 1.17x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 80.4 ms: 1.17x faster                                                        |
| sympy_str               | 325 ms                                                 | 284 ms: 1.14x faster                                                         |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                        |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                                        |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 99.5 ms: 1.12x faster                                                        |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                         |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                                         |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.08x faster                                                         |
| telco                   | 6.73 ms                                                | 6.39 ms: 1.05x faster                                                        |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                                        |
| async_generators        | 426 ms                                                 | 409 ms: 1.04x faster                                                         |
| regex_dna               | 214 ms                                                 | 216 ms: 1.01x slower                                                         |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| unpickle_list           | 4.92 us                                                | 5.02 us: 1.02x slower                                                        |
| gc_traversal            | 3.53 ms                                                | 3.85 ms: 1.09x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.52 ms: 1.10x slower                                                        |
| pickle_dict             | 27.6 us                                                | 30.9 us: 1.12x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                        |
| dask                    | 436 ms                                                 | 503 ms: 1.15x slower                                                         |
| coverage                | 74.7 ms                                                | 98.2 ms: 1.31x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
