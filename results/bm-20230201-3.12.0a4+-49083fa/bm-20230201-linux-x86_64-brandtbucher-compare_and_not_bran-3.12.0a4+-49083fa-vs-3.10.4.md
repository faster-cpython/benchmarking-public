
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 49083fa
- commit date: 2023-02-01
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.33x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.47 ms: 1.42x faster                                                        |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.9 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.4 ms: 1.52x faster                                                        |
| float          | 109 ms                                                 | 72.7 ms: 1.50x faster                                                        |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                        |
| regex_dna      | 214 ms                                                 | 217 ms: 1.01x slower                                                         |
| regex_effbot   | 3.19 ms                                                | 3.63 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 202 us: 1.49x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.33 ms: 1.44x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 78.0 ms: 1.20x faster                                                        |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| pickle_list          | 4.72 us                                                | 4.31 us: 1.10x faster                                                        |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                                         |
| unpickle_list        | 4.92 us                                                | 5.02 us: 1.02x slower                                                        |
| pickle_dict          | 27.6 us                                                | 32.2 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.88 ms: 1.59x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.43 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.75 ms: 1.50x faster                                                        |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                        |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 46.3 ms: 1.38x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.25 ms: 2.24x faster                                                        |
| logging_silent          | 176 ns                                                 | 92.7 ns: 1.90x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 494 ms: 1.85x faster                                                         |
| richards                | 75.2 ms                                                | 41.5 ms: 1.81x faster                                                        |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                                         |
| pyflate                 | 676 ms                                                 | 402 ms: 1.68x faster                                                         |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                         |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                 | 66.1 ms: 1.64x faster                                                        |
| chaos                   | 106 ms                                                 | 64.7 ms: 1.63x faster                                                        |
| spectral_norm           | 150 ms                                                 | 93.4 ms: 1.60x faster                                                        |
| hexiom                  | 9.43 ms                                                | 5.92 ms: 1.59x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.88 ms: 1.59x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 73.7 ms: 1.58x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                                         |
| scimark_lu              | 161 ms                                                 | 105 ms: 1.53x faster                                                         |
| nbody                   | 144 ms                                                 | 94.4 ms: 1.52x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                                        |
| mako                    | 14.7 ms                                                | 9.75 ms: 1.50x faster                                                        |
| float                   | 109 ms                                                 | 72.7 ms: 1.50x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 202 us: 1.49x faster                                                         |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.33 ms: 1.44x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                        |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.47 ms: 1.42x faster                                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 674 ms: 1.41x faster                                                         |
| logging_simple          | 8.10 us                                                | 5.77 us: 1.40x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                        |
| scimark_fft             | 421 ms                                                 | 302 ms: 1.39x faster                                                         |
| logging_format          | 8.85 us                                                | 6.38 us: 1.39x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 43.0 ns: 1.38x faster                                                        |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 46.3 ms: 1.38x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.98 ms: 1.37x faster                                                        |
| deepcopy                | 438 us                                                 | 321 us: 1.37x faster                                                         |
| thrift                  | 1.03 ms                                                | 758 us: 1.36x faster                                                         |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                                         |
| tornado_http            | 128 ms                                                 | 94.9 ms: 1.35x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 996 us: 1.35x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                       |
| async_tree_memoization  | 855 ms                                                 | 641 ms: 1.33x faster                                                         |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                       |
| fannkuch                | 488 ms                                                 | 367 ms: 1.33x faster                                                         |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                                        |
| 2to3                    | 335 ms                                                 | 253 ms: 1.33x faster                                                         |
| deepcopy_reduce         | 3.79 us                                                | 2.88 us: 1.32x faster                                                        |
| nqueens                 | 100 ms                                                 | 76.6 ms: 1.31x faster                                                        |
| sqlglot_optimize        | 65.2 ms                                                | 50.9 ms: 1.28x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 753 ms: 1.26x faster                                                         |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 781 us: 1.21x faster                                                         |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                                        |
| async_generators        | 426 ms                                                 | 353 ms: 1.21x faster                                                         |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                         |
| xml_etree_generate      | 93.8 ms                                                | 78.0 ms: 1.20x faster                                                        |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                        |
| coroutines              | 31.6 ms                                                | 26.4 ms: 1.20x faster                                                        |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.18x faster                                                         |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                         |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                        |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                        |
| djangocms               | 36.9 us                                                | 32.7 us: 1.13x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| pickle_list             | 4.72 us                                                | 4.31 us: 1.10x faster                                                        |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                       |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                         |
| telco                   | 6.73 ms                                                | 6.44 ms: 1.05x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                                         |
| generators              | 76.4 ms                                                | 77.3 ms: 1.01x slower                                                        |
| regex_dna               | 214 ms                                                 | 217 ms: 1.01x slower                                                         |
| unpickle_list           | 4.92 us                                                | 5.02 us: 1.02x slower                                                        |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                         |
| python_startup_no_site  | 5.78 ms                                                | 6.43 ms: 1.11x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.63 ms: 1.14x slower                                                        |
| dask                    | 436 ms                                                 | 507 ms: 1.16x slower                                                         |
| pickle_dict             | 27.6 us                                                | 32.2 us: 1.17x slower                                                        |
| gc_traversal            | 3.53 ms                                                | 4.27 ms: 1.21x slower                                                        |
| coverage                | 74.7 ms                                                | 100 ms: 1.34x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-49083fa/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-49083fa.json: mypy
