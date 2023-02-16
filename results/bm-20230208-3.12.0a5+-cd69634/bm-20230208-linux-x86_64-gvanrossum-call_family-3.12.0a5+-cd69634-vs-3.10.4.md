
# Results vs. 3.10.4

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: cd69634
- commit date: 2023-02-08
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                              |
| chameleon      | 9.17 ms                                                | 6.44 ms: 1.42x faster                                             |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                            |
| html5lib       | 85.9 ms                                                | 60.7 ms: 1.41x faster                                             |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                             |
| Geometric mean | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.6 ms: 1.52x faster                                             |
| float          | 109 ms                                                 | 74.0 ms: 1.47x faster                                             |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.31x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                              |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.20x faster                                             |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                              |
| regex_effbot   | 3.19 ms                                                | 3.64 ms: 1.14x slower                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                              |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.51x faster                                              |
| json_dumps           | 13.4 ms                                                | 9.44 ms: 1.42x faster                                             |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                             |
| xml_etree_generate   | 93.8 ms                                                | 77.1 ms: 1.22x faster                                             |
| json_loads           | 28.7 us                                                | 23.8 us: 1.20x faster                                             |
| pickle_list          | 4.72 us                                                | 4.03 us: 1.17x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                              |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                             |
| unpickle_list        | 4.92 us                                                | 4.97 us: 1.01x slower                                             |
| pickle_dict          | 27.6 us                                                | 30.3 us: 1.10x slower                                             |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                      |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.91 ms: 1.58x faster                                             |
| python_startup_no_site | 5.78 ms                                                | 6.47 ms: 1.12x slower                                             |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                             |
| mako            | 14.7 ms                                                | 9.97 ms: 1.47x faster                                             |
| django_template | 46.3 ms                                                | 33.2 ms: 1.40x faster                                             |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                             |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.17 ms: 2.30x faster                                             |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                              |
| asyncio_tcp             | 914 ms                                                 | 490 ms: 1.87x faster                                              |
| logging_silent          | 176 ns                                                 | 96.3 ns: 1.83x faster                                             |
| richards                | 75.2 ms                                                | 42.3 ms: 1.78x faster                                             |
| pyflate                 | 676 ms                                                 | 407 ms: 1.66x faster                                              |
| scimark_monte_carlo     | 109 ms                                                 | 65.8 ms: 1.65x faster                                             |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                              |
| raytrace                | 467 ms                                                 | 288 ms: 1.62x faster                                              |
| crypto_pyaes            | 117 ms                                                 | 72.7 ms: 1.60x faster                                             |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                              |
| chaos                   | 106 ms                                                 | 66.7 ms: 1.58x faster                                             |
| python_startup          | 14.1 ms                                                | 8.91 ms: 1.58x faster                                             |
| hexiom                  | 9.43 ms                                                | 6.02 ms: 1.57x faster                                             |
| spectral_norm           | 150 ms                                                 | 96.1 ms: 1.56x faster                                             |
| nbody                   | 144 ms                                                 | 94.6 ms: 1.52x faster                                             |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.51x faster                                              |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                             |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.48x faster                                              |
| deepcopy_memo           | 51.7 us                                                | 34.9 us: 1.48x faster                                             |
| float                   | 109 ms                                                 | 74.0 ms: 1.47x faster                                             |
| mako                    | 14.7 ms                                                | 9.97 ms: 1.47x faster                                             |
| json_dumps              | 13.4 ms                                                | 9.44 ms: 1.42x faster                                             |
| chameleon               | 9.17 ms                                                | 6.44 ms: 1.42x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                             |
| html5lib                | 85.9 ms                                                | 60.7 ms: 1.41x faster                                             |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                            |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                             |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.40x faster                                             |
| thrift                  | 1.03 ms                                                | 740 us: 1.40x faster                                              |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.40x faster                                             |
| pprint_pformat          | 1.98 sec                                               | 1.43 sec: 1.39x faster                                            |
| scimark_fft             | 421 ms                                                 | 305 ms: 1.38x faster                                              |
| logging_simple          | 8.10 us                                                | 5.88 us: 1.38x faster                                             |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                              |
| logging_format          | 8.85 us                                                | 6.46 us: 1.37x faster                                             |
| fannkuch                | 488 ms                                                 | 356 ms: 1.37x faster                                              |
| pprint_safe_repr        | 953 ms                                                 | 697 ms: 1.37x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                             |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                             |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                              |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                             |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                            |
| async_tree_memoization  | 855 ms                                                 | 637 ms: 1.34x faster                                              |
| unpack_sequence         | 59.4 ns                                                | 44.4 ns: 1.34x faster                                             |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                              |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                             |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                             |
| deepcopy                | 438 us                                                 | 332 us: 1.32x faster                                              |
| coroutines              | 31.6 ms                                                | 24.3 ms: 1.30x faster                                             |
| mypy2                   | 430 ms                                                 | 331 ms: 1.30x faster                                              |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                             |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                            |
| sqlglot_optimize        | 65.2 ms                                                | 51.4 ms: 1.27x faster                                             |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                              |
| nqueens                 | 100 ms                                                 | 79.2 ms: 1.26x faster                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 752 ms: 1.26x faster                                              |
| async_generators        | 426 ms                                                 | 346 ms: 1.23x faster                                              |
| xml_etree_generate      | 93.8 ms                                                | 77.1 ms: 1.22x faster                                             |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                             |
| bench_thread_pool       | 946 us                                                 | 783 us: 1.21x faster                                              |
| json_loads              | 28.7 us                                                | 23.8 us: 1.20x faster                                             |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                              |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                              |
| dulwich_log             | 75.8 ms                                                | 63.4 ms: 1.20x faster                                             |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.20x faster                                             |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.1 ms: 1.18x faster                                             |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.18x faster                                              |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.17x faster                                              |
| pickle_list             | 4.72 us                                                | 4.03 us: 1.17x faster                                             |
| djangocms               | 36.9 us                                                | 31.8 us: 1.16x faster                                             |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                             |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                             |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.13x faster                                             |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                              |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                             |
| mdp                     | 2.74 sec                                               | 2.48 sec: 1.10x faster                                            |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                              |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                             |
| meteor_contest          | 114 ms                                                 | 107 ms: 1.07x faster                                              |
| generators              | 76.4 ms                                                | 72.1 ms: 1.06x faster                                             |
| telco                   | 6.73 ms                                                | 6.36 ms: 1.06x faster                                             |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                              |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                              |
| unpickle_list           | 4.92 us                                                | 4.97 us: 1.01x slower                                             |
| pickle_dict             | 27.6 us                                                | 30.3 us: 1.10x slower                                             |
| python_startup_no_site  | 5.78 ms                                                | 6.47 ms: 1.12x slower                                             |
| regex_effbot            | 3.19 ms                                                | 3.64 ms: 1.14x slower                                             |
| gc_traversal            | 3.53 ms                                                | 4.17 ms: 1.18x slower                                             |
| coverage                | 74.7 ms                                                | 98.8 ms: 1.32x slower                                             |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                      |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
